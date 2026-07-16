#!/usr/bin/env python3
"""Extract deterministic component evidence from a Sketch file and merge approved rules."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
import zipfile
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]


def first_existing(*paths: Path) -> Path:
    for path in paths:
        if path.exists():
            return path
    return paths[0]


DEFAULT_SKETCH = first_existing(
    ROOT / "codex-skills/supervision-page-builder/references/sketch/监管平台.sketch",
    ROOT / "install/codex-skills/supervision-platform-ai-skill/references/sketch/监管平台.sketch",
    ROOT / "references/sketch/监管平台.sketch",
)
DEFAULT_MAPPING = ROOT / "data/sketch-contract/component-map.json"
DEFAULT_OVERRIDES = ROOT / "data/sketch-contract/manual-overrides.json"
DEFAULT_OUTPUT = ROOT / "data/sketch-component-contract.json"
DEFAULT_CONFLICTS = ROOT / "data/sketch-contract-conflicts.json"
DEFAULT_DOCS = ROOT / ("knowledge/component-parameters" if (ROOT / "knowledge").exists() else "rules/component-parameters")

REQUIRED_COMPONENT_FIELDS = (
    "componentName",
    "sourceSymbolId",
    "sourceArtboardId",
    "dimensions",
    "spacing",
    "appearance",
    "typography",
    "states",
    "layout",
    "responsive",
    "evidence",
    "confidence",
    "override",
)


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def stable_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def walk_layers(layer: dict[str, Any]) -> Iterable[dict[str, Any]]:
    yield layer
    for child in layer.get("layers", []) or []:
        yield from walk_layers(child)


def frame_of(layer: dict[str, Any]) -> dict[str, Any]:
    frame = layer.get("frame") or {}
    return {key: frame.get(key) for key in ("x", "y", "width", "height") if frame.get(key) is not None}


def color_value(color: dict[str, Any] | None) -> dict[str, float] | None:
    if not color:
        return None
    return {
        "red": round(float(color.get("red", 0)), 4),
        "green": round(float(color.get("green", 0)), 4),
        "blue": round(float(color.get("blue", 0)), 4),
        "alpha": round(float(color.get("alpha", 1)), 4),
    }


def unique_dicts(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    output: list[dict[str, Any]] = []
    for item in items:
        key = json.dumps(item, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            seen.add(key)
            output.append(item)
    return output


def summarize_appearance(layer: dict[str, Any]) -> dict[str, Any]:
    fills: list[dict[str, Any]] = []
    borders: list[dict[str, Any]] = []
    shadows: list[dict[str, Any]] = []
    blurs: list[dict[str, Any]] = []
    radii: list[dict[str, Any]] = []
    for node in walk_layers(layer):
        style = node.get("style") or {}
        for fill in style.get("fills", []) or []:
            if fill.get("isEnabled", True):
                fills.append({"fillType": fill.get("fillType"), "color": color_value(fill.get("color"))})
        for border in style.get("borders", []) or []:
            if border.get("isEnabled", True):
                borders.append({"thickness": border.get("thickness"), "position": border.get("position"), "color": color_value(border.get("color"))})
        for shadow in (style.get("shadows", []) or []) + (style.get("innerShadows", []) or []):
            if shadow.get("isEnabled", True):
                shadows.append({"blurRadius": shadow.get("blurRadius"), "offsetX": shadow.get("offsetX"), "offsetY": shadow.get("offsetY"), "spread": shadow.get("spread"), "color": color_value(shadow.get("color"))})
        blur = style.get("blur") or {}
        if blur.get("isEnabled"):
            blurs.append({"type": blur.get("type"), "radius": blur.get("radius")})
        if node.get("fixedRadius") is not None:
            radii.append({"fixedRadius": node.get("fixedRadius")})
        if node.get("cornerRadius") is not None:
            radii.append({"cornerRadius": node.get("cornerRadius")})
    return {
        "observedFills": unique_dicts(fills),
        "observedBorders": unique_dicts(borders),
        "observedShadows": unique_dicts(shadows),
        "observedBlurs": unique_dicts(blurs),
        "observedRadii": unique_dicts(radii),
    }


def summarize_typography(layer: dict[str, Any]) -> list[dict[str, Any]]:
    text_styles: list[dict[str, Any]] = []
    for node in walk_layers(layer):
        if node.get("_class") != "text":
            continue
        attributed = node.get("attributedString") or {}
        for span in attributed.get("attributes", []) or []:
            attrs = span.get("attributes") or {}
            font = ((attrs.get("MSAttributedStringFontAttribute") or {}).get("attributes") or {})
            paragraph = attrs.get("paragraphStyle") or {}
            text_styles.append({
                "fontName": font.get("name"),
                "fontSize": font.get("size"),
                "lineHeight": paragraph.get("maximumLineHeight") or paragraph.get("minimumLineHeight"),
                "textColor": color_value(attrs.get("MSAttributedStringColorAttribute")),
            })
    return unique_dicts([item for item in text_styles if any(value is not None for value in item.values())])


def summarize_layer(layer: dict[str, Any]) -> dict[str, Any]:
    direct_children = layer.get("layers", []) or []
    return {
        "id": layer.get("do_objectID"),
        "name": layer.get("name"),
        "class": layer.get("_class"),
        "frame": frame_of(layer),
        "resizingConstraint": layer.get("resizingConstraint"),
        "directChildFrames": [frame_of(child) for child in direct_children if frame_of(child)],
        "appearance": summarize_appearance(layer),
        "typography": summarize_typography(layer),
    }


def load_sketch(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    with zipfile.ZipFile(path) as archive:
        meta = json.loads(archive.read("meta.json"))
        symbol_masters: list[dict[str, Any]] = []
        artboards: list[dict[str, Any]] = []
        for member in sorted(name for name in archive.namelist() if name.startswith("pages/") and name.endswith(".json")):
            page = json.loads(archive.read(member))
            for layer in page.get("layers", []) or []:
                if layer.get("_class") == "symbolMaster":
                    symbol_masters.append(layer)
                elif layer.get("_class") == "artboard":
                    artboards.append(layer)
    return meta, symbol_masters, artboards


def matches(name: str, patterns: list[str]) -> bool:
    return any(pattern in name for pattern in patterns)


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result


def build_contract(sketch_path: Path, mapping: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    meta, symbols, artboards = load_sketch(sketch_path)
    components: dict[str, Any] = {}
    for component_name, route in mapping["components"].items():
        matched_symbols = [symbol for symbol in symbols if matches(symbol.get("name", ""), route.get("symbolNamePatterns", []))]
        matched_artboards = [artboard for artboard in artboards if matches(artboard.get("name", ""), route.get("artboardNamePatterns", []))]
        evidence: list[dict[str, Any]] = []
        evidence.extend({"type": "sketch-symbol", "id": item.get("do_objectID"), "name": item.get("name"), "relativePath": "references/sketch/监管平台.sketch"} for item in matched_symbols)
        evidence.extend({"type": "sketch-artboard", "id": item.get("do_objectID"), "name": item.get("name"), "relativePath": "references/sketch/监管平台.sketch"} for item in matched_artboards)
        evidence.append({"type": "golden-demo", "relativePath": "golden-demo/supervision-warning-supervise-query.html"})
        base = {
            "componentName": component_name,
            "category": route["category"],
            "sourceSymbolId": sorted(item.get("do_objectID") for item in matched_symbols if item.get("do_objectID")),
            "sourceArtboardId": sorted(item.get("do_objectID") for item in matched_artboards if item.get("do_objectID")),
            "dimensions": {},
            "spacing": {},
            "appearance": {},
            "typography": {},
            "states": {},
            "layout": {},
            "responsive": {},
            "evidence": evidence,
            "sketchObserved": {
                "symbols": [summarize_layer(item) for item in matched_symbols],
                "artboards": [{"id": item.get("do_objectID"), "name": item.get("name"), "frame": frame_of(item)} for item in matched_artboards],
            },
            "confidence": "auto-extracted",
            "override": {"applied": False, "reason": "No approved override supplied."},
        }
        components[component_name] = deep_merge(base, overrides.get("components", {}).get(component_name, {}))

    digest = hashlib.sha256(sketch_path.read_bytes()).hexdigest()
    contract = {
        "schemaVersion": "1.0.0",
        "contractVersion": "1.0.0",
        "source": {
            "logicalPath": "references/sketch/监管平台.sketch",
            "locatorCandidates": [
                "codex-skills/supervision-page-builder/references/sketch/监管平台.sketch",
                "install/codex-skills/supervision-platform-ai-skill/references/sketch/监管平台.sketch",
                "references/sketch/监管平台.sketch"
            ],
            "sha256": digest,
            "sketchAppVersion": meta.get("appVersion"),
            "sketchFormatVersion": meta.get("version"),
        },
        "priority": overrides["priority"],
        "normativeColorRule": "Normative appearance values must use existing Theme or DCP component tokens. Raw Sketch colors may appear only under sketchObserved evidence.",
        "components": components,
    }
    validate_contract(contract, mapping)
    return contract


def validate_contract(contract: dict[str, Any], mapping: dict[str, Any]) -> None:
    errors: list[str] = []
    for name in mapping["components"]:
        component = contract["components"].get(name)
        if not component:
            errors.append(f"missing component: {name}")
            continue
        for field in REQUIRED_COMPONENT_FIELDS:
            if field not in component:
                errors.append(f"{name}: missing field {field}")
        for field in ("dimensions", "spacing", "appearance", "typography", "states", "layout", "responsive"):
            if not component.get(field):
                errors.append(f"{name}: empty required section {field}")
    if errors:
        raise ValueError("Contract validation failed:\n- " + "\n- ".join(errors))


def human(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return "`" + json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "`"
    return str(value)


def render_component(component: dict[str, Any]) -> str:
    lines = [f"## {component['componentName']}", "", f"- 置信度：`{component['confidence']}`", f"- 分类：`{component['category']}`"]
    if component["sourceSymbolId"]:
        lines.append(f"- Sketch Symbol：{', '.join(f'`{item}`' for item in component['sourceSymbolId'])}")
    if component["sourceArtboardId"]:
        lines.append(f"- Sketch 画板：{', '.join(f'`{item}`' for item in component['sourceArtboardId'])}")
    lines.extend(["", "| 参数组 | 最终规范 |", "| --- | --- |"])
    for key in ("dimensions", "spacing", "appearance", "typography", "states", "layout", "responsive"):
        lines.append(f"| `{key}` | {human(component[key])} |")
    lines.extend(["", f"覆盖说明：{component['override'].get('reason', '无')}", ""])
    return "\n".join(lines)


def write_docs(contract: dict[str, Any], mapping: dict[str, Any], docs_dir: Path) -> None:
    docs_dir.mkdir(parents=True, exist_ok=True)
    titles = {
        "page-shell-navigation": "页面骨架与导航参数",
        "filter-form": "筛选区、表单与按钮参数",
        "table-status-actions": "表格、状态与操作参数",
        "modal-drawer": "弹窗与抽屉参数",
        "data-display": "数据展示参数",
    }
    index_lines = ["# Sketch 结构化组件参数", "", "本目录由 `data/sketch-component-contract.json` 自动生成，禁止单独手改。", "", "按任务读取："]
    for group, component_names in mapping["documentGroups"].items():
        title = titles[group]
        filename = f"{group}.md"
        content = [f"# {title}", "", "最终参数优先于 Sketch 原始观测值；颜色必须使用已有 Theme/DCP token。", ""]
        for name in component_names:
            content.append(render_component(contract["components"][name]))
        (docs_dir / filename).write_text("\n".join(content).rstrip() + "\n", encoding="utf-8")
        index_lines.append(f"- `{filename}`：{title}")
    (docs_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sketch", type=Path, default=DEFAULT_SKETCH)
    parser.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING)
    parser.add_argument("--overrides", type=Path, default=DEFAULT_OVERRIDES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--conflicts", type=Path, default=DEFAULT_CONFLICTS)
    parser.add_argument("--docs-dir", type=Path, default=DEFAULT_DOCS)
    parser.add_argument("--check", action="store_true", help="Fail when generated outputs differ from files on disk.")
    args = parser.parse_args()

    mapping = read_json(args.mapping)
    overrides = read_json(args.overrides)
    contract = build_contract(args.sketch, mapping, overrides)
    unresolved = [item for item in overrides.get("knownConflicts", []) if item.get("status") != "resolved"]
    if unresolved:
        names = ", ".join(f"{item.get('component')}.{item.get('property')}" for item in unresolved)
        print("Unresolved core component conflicts: " + names, file=sys.stderr)
        return 1
    contract_text = stable_json(contract)
    conflicts_text = stable_json({"schemaVersion": "1.0.0", "priority": overrides["priority"], "conflicts": overrides.get("knownConflicts", [])})

    if args.check:
        mismatches = []
        for path, expected in ((args.output, contract_text), (args.conflicts, conflicts_text)):
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                mismatches.append(str(path))
        with tempfile.TemporaryDirectory() as temp_dir:
            generated_docs = Path(temp_dir)
            write_docs(contract, mapping, generated_docs)
            for expected_path in sorted(generated_docs.glob("*.md")):
                actual_path = args.docs_dir / expected_path.name
                if not actual_path.exists() or actual_path.read_text(encoding="utf-8") != expected_path.read_text(encoding="utf-8"):
                    mismatches.append(str(actual_path))
        if mismatches:
            print("Generated outputs are stale: " + ", ".join(mismatches), file=sys.stderr)
            return 1
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(contract_text, encoding="utf-8")
    args.conflicts.write_text(conflicts_text, encoding="utf-8")
    write_docs(contract, mapping, args.docs_dir)
    print(f"Generated {len(contract['components'])} component contracts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

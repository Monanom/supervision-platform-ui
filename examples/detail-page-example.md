# Detail Page Example

监管对象详情页：

## 页面类型

DetailPage

## Page Recipe

PageHeader -> OverviewCard -> DescriptionList -> RelatedTable / Timeline

## 组件映射

- PageHeader：说明当前对象名称、监管类型和返回入口。
- OverviewCard：展示关键状态、风险等级、责任主体、最近更新时间。暂按 InfoCard 承载。
- DescriptionList：展示主体信息、监管信息、处理信息等字段。
- RelatedTable：展示关联项目、关联风险、关联记录等表格信息，暂按 DataTable 承载。
- Timeline：展示操作记录或流转记录。TODO：KB 未定义字段结构。
- StatusTag：表达状态，不作为操作按钮。

## 阅读顺序

概要 -> 主体信息 -> 关联信息 -> 操作记录

## 校验重点

- 保留原 Demo 的字段名称和值。
- 详情页不做营销式大标题。
- 关联信息优先使用表格，不改成电商风卡片。
- Card 圆角 8px，Dialog / Drawer 圆角 12px。

# Dashboard Example

监管态势总览页：

## 页面类型

Dashboard

## Page Recipe

PageHeader -> StatisticPanel -> TrendChart / AnalysisPanel -> BusinessTable

## 组件映射

- PageHeader：说明当前监管主题、统计范围和更新时间。
- StatisticPanel：第一屏必须出现，用 4-8 个指标展示总体态势，例如监管对象总数、异常数量、待处理事项、今日新增风险。
- TrendChart：展示风险趋势或处理趋势。TODO：KB 未定义图表类型和图表色板，禁止使用彩虹图表。
- AnalysisPanel：展示重点风险或异常分布。TODO：KB 未定义独立结构。
- BusinessTable：展示详细数据，暂按 DataTable 承载。
- StatusTag：用于表达风险状态、处理状态。

## 阅读顺序

总体态势 -> 重点风险 -> 趋势变化 -> 详细数据

## 校验重点

- Dashboard 第一屏必须有 StatisticPanel。
- 数字优先，装饰克制。
- 颜色用于状态表达，不用于装饰。
- 不得使用 Hero Banner、营销大标题、大渐变、毛玻璃和彩色阴影。

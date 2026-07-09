# List Page Example

项目预警列表页：

## 页面类型

ListPage

## Page Recipe

PageHeader -> SearchPanel -> StatisticPanel(optional) -> Toolbar -> DataTable -> Pagination

## 组件映射

- PageHeader：说明页面为项目预警列表，并保留监管范围。
- SearchPanel：承载项目名称、区域、风险等级、处理状态、时间范围等筛选条件。
- StatisticPanel：可选，用于展示全部预警、待处理、高风险、已处置等统计。
- Toolbar：承载批量处理、导出、刷新等表格操作。
- DataTable：展示项目、责任主体、风险等级、状态、发生时间、处理人、操作入口。
- StatusTag：表达风险等级和处理状态，不作为按钮。
- Pagination：用于列表分页。

## 校验重点

- List 页必须出现 SearchPanel。
- DataTable 是业务主体，不能用卡片流替代表格。
- 不得删除筛选项、表格列和操作入口。
- 按钮、标签、输入框圆角为 4px；页面间距为 20px；表格行高为 44px。

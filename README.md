# AI 股票分析仪表盘
> 基于 Python + Streamlit 打造的实时股票数据分析与 AI 预测平台，整合实时数据获取、技术指标可视化、时序预测、风险评分与财经情感分析，一站式支撑金融量化与投资决策。
---
## 🌟 项目亮点
- 实时股票数据拉取与自动更新
- 股价、均线、RSI 等多维度图表展示
- AI时序模型预测未来股价趋势
- 智能风险量化分析与等级判定
- 财经新闻情感分析（扩展模块）
- 轻量 Web 界面，开箱即用
## 🛠 技术栈
- 语言：Python
- 框架：Streamlit（交互式看板）
- 数据源：yFinance
- 预测模型：Prophet
- 数据处理：Pandas
- 可视化：Matplotlib / Plotly
---
## 🚀 快速开始
1. 克隆项目
``` bash
  git clone https://github.com/yourname/ai-stock-analysis.git 
  cd ai-stock-analysis
```
2. 安装依赖
``` bash
pip install -r requirements.txt
```
3. 运行项目
``` bash
streamlit run app.py
```
---
## 📊 功能说明
- 实时行情：输入股票代码（如 AAPL）查看最新股价与历史走势
- 技术指标：MA20/MA50 均线、RSI 指标可视化
- AI 预测：Prophet 模型生成未来股价预测曲线
- 风险分析：自动计算风险评分并判定等级（低 / 中 / 高）
- 情感分析：基于财经新闻标题做多空情绪判断

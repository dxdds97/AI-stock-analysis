import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.data_loader import load_stock_data
from utils.indicators import add_indicators
from utils.risk import calculate_risk
from models.prophet_model import run_prophet
# from models.lstm_model import run_lstm

st.set_page_config(page_title="AI Stock Dashboard", layout="wide")

st.title("📈 AI Stock Analysis Dashboard")

# 输入股票代码
ticker = st.text_input("Enter Stock Ticker", "AAPL")

# 数据加载（缓存）
@st.cache_data
def get_data(ticker):
    df = load_stock_data(ticker)

    if df is None or df.empty:
        return pd.DataFrame()

    #  统一列结构（解决 MultiIndex）
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    #  清理数据
    df = df.dropna(how="all")

    #  转数值（避免 rolling 报错）
    df = df.apply(pd.to_numeric, errors='ignore')

    return df

data = get_data(ticker)


if data.empty:
    st.error("No data found!")
    st.stop()

# 添加指标
data = add_indicators(data)

# ===== 基础数据展示 =====
st.subheader("📊 Stock Price")
st.line_chart(data['Close'])

# ===== 技术指标 =====
st.subheader("📉 Moving Averages")
st.line_chart(data[['Close', 'MA20', 'MA50']])

# ===== RSI =====
st.subheader("📌 RSI Indicator")
st.line_chart(data['RSI'])

# ===== 风险评分 =====
risk_score, level = calculate_risk(data)

st.subheader("⚠️ Risk Analysis")
st.metric("Risk Score", f"{risk_score:.2f}")
st.write(f"Risk Level: **{level}**")

# ===== Prophet预测 =====
st.subheader("🔮 AI Forecast")

forecast = run_prophet(data)

fig, ax = plt.subplots()
ax.plot(forecast['ds'], forecast['yhat'], label='Prediction')
ax.set_title("Future Price Prediction")
ax.legend()

st.pyplot(fig)


# st.subheader("🔮 AI Forecast (LSTM)")
#
# forecast = run_lstm(data)
#
# fig, ax = plt.subplots()
#
# # 历史数据
# ax.plot(data.index, data['Close'], label='History')
#
# # 预测数据
# ax.plot(forecast['ds'], forecast['yhat'], label='Prediction')
#
# ax.set_title("LSTM Price Prediction")
# ax.legend()
#
# st.pyplot(fig)
# ===== 自动分析结论 =====
st.subheader("🧠 AI Insight")

latest_price = data['Close'].iloc[-1]
ma20 = data['MA20'].iloc[-1]

if latest_price > ma20:
    trend = "Uptrend 📈"
else:
    trend = "Downtrend 📉"

st.write(f"- Current Trend: **{trend}**")
st.write(f"- Risk Level: **{level}**")

if level == "High":
    st.warning("High volatility detected. Trade carefully!")
elif level == "Medium":
    st.info("Moderate risk.")
else:
    st.success("Low risk stock.")
import numpy as np

def calculate_risk(df):
    returns = df['Close'].pct_change().dropna()

    volatility = np.std(returns) * 252**0.5  # 年化波动率

    # 风险评分（0-100）
    risk_score = min(volatility * 100, 100)

    if risk_score < 20:
        level = "Low"
    elif risk_score < 50:
        level = "Medium"
    else:
        level = "High"

    return risk_score, level
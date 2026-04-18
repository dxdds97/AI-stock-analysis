from prophet import Prophet
import pandas as pd

def run_prophet(df, periods=30):
    data = df.reset_index()[['Date', 'Close']]
    data.columns = ['ds', 'y']

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast
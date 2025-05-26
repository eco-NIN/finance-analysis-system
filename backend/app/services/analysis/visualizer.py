import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

def plot_stock_trend(df: pd.DataFrame) -> str:
    plt.figure(figsize=(10, 4))
    plt.plot(df["trade_date"], df["close"], label="Close Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Stock Price Trend")
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates

import io
import base64
import pandas as pd
matplotlib.use('Agg')
def plot_stock_trend(df: pd.DataFrame) -> str:
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    plt.figure(figsize=(10, 4))
    plt.plot(df["trade_date"], df["close"], label="Close Price")

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Stock Price Trend")
    plt.legend()

    locator = mdates.AutoDateLocator(minticks=5, maxticks=10)
    formatter = mdates.DateFormatter('%Y-%m-%d')

    ax = plt.gca()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')


def plot_volume(df: pd.DataFrame) -> str:
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    plt.figure(figsize=(10, 3))
    plt.bar(df["trade_date"], df["vol"], color='skyblue')
    plt.tight_layout()
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.title("Daily Trading Volume")
    plt.tight_layout()
    locator = mdates.AutoDateLocator(minticks=5, maxticks=10)
    formatter = mdates.DateFormatter('%Y-%m-%d')

    ax = plt.gca()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')


def plot_daily_returns_scatter(df: pd.DataFrame) -> str:
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    df = df.sort_values("trade_date")

    # 计算每日涨跌幅（百分比）
    df['daily_return'] = df['close'].pct_change() * 100

    plt.figure(figsize=(10, 4))
    plt.scatter(df['trade_date'], df['daily_return'], color='blue', alpha=0.6, s=20)
    plt.axhline(0, color='red', linestyle='--', linewidth=1)  # 零涨跌线
    plt.title("Daily Return Scatter Plot")
    plt.xlabel("Date")
    plt.ylabel("Daily Return (%)")

    locator = mdates.AutoDateLocator(minticks=5, maxticks=10)
    formatter = mdates.DateFormatter('%Y-%m-%d')

    ax = plt.gca()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45)

    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def plot_moving_averages(df: pd.DataFrame) -> str:
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    df = df.sort_values("trade_date")

    df['MA5'] = df['close'].rolling(window=5).mean()
    df['MA10'] = df['close'].rolling(window=10).mean()

    plt.figure(figsize=(10, 4))
    plt.plot(df['trade_date'], df['close'], label='Close Price')
    plt.plot(df['trade_date'], df['MA5'], label='MA5')
    plt.plot(df['trade_date'], df['MA10'], label='MA10')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Close Price with Moving Averages')
    plt.legend()

    locator = mdates.AutoDateLocator(minticks=5, maxticks=10)
    formatter = mdates.DateFormatter('%Y-%m-%d')

    ax = plt.gca()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')


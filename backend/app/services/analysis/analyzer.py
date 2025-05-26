from app.services.analysis.data_fetcher import fetch_stock_data
from app.services.analysis.visualizer import plot_stock_trend
from app.services.analysis.visualizer import plot_volume
from app.services.analysis.visualizer import plot_daily_returns_scatter
from app.services.analysis.visualizer import plot_moving_averages
def analyze_stock_data(stock_code, start_date, end_date):
    raw_df = fetch_stock_data(stock_code, start_date, end_date)
    # cleaned_df = clean_data(raw_df)   # 删除调用清洗函数这一行
    # 直接用原始数据 raw_df
    image_base64_1 = plot_stock_trend(raw_df)
    image_base64_2 = plot_volume(raw_df)
    image_base64_3 = plot_daily_returns_scatter(raw_df)
    image_base64_4 = plot_moving_averages(raw_df)
    returns = raw_df["close"].pct_change().dropna()
    rolling_max = raw_df["close"].cummax()
    summary = {
        "average_close": float(raw_df["close"].mean()),
        "max_close": float(raw_df["close"].max()),
        "min_close": float(raw_df["close"].min()),
        "volatility": float(returns.std()),
        "average_daily_return": float(returns.mean()),
        "max_drawdown": float(((raw_df["close"] - rolling_max) / rolling_max).min()),
        "total_return": float((raw_df["close"].iloc[-1] / raw_df["close"].iloc[0]) - 1),
        "average_volume": float(raw_df["vol"].mean()),
        "max_volume": float(raw_df["vol"].max()),
        "min_volume": float(raw_df["vol"].min()),
        "up_days": int((raw_df["pct_chg"] > 0).sum()),
        "down_days": int((raw_df["pct_chg"] < 0).sum())
    }
    return summary, image_base64_1,image_base64_2, image_base64_3, image_base64_4

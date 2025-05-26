from app.services.analysis.data_fetcher import fetch_stock_data
from app.services.analysis.visualizer import plot_stock_trend

def analyze_stock_data(stock_code, start_date, end_date):
    raw_df = fetch_stock_data(stock_code, start_date, end_date)
    # cleaned_df = clean_data(raw_df)   # 删除调用清洗函数这一行
    # 直接用原始数据 raw_df
    image_base64 = plot_stock_trend(raw_df)
    summary = {
        "average_close": float(raw_df["close"].mean()),
        "max_close": float(raw_df["close"].max()),
        "min_close": float(raw_df["close"].min())
    }
    return summary, image_base64

# @Author  : eco
# @Date    :2025/6/7 16:19
# @Function:
# app/services/prediction/extractor.py
import json
from app.models.prediction import RawData
import pandas as pd
import requests
from datetime import datetime, timedelta

def fetch_dongfang_data(
        stock_code: str,
        data_type: str,
        start_date: str = None,  # 新增：开始日期（格式：YYYYMMDD）
        end_date: str = None  # 新增：结束日期
) -> pd.DataFrame:
    """
    从东方财富网获取股票的历史行情数据
    参数：
        stock_code: 股票代码（如 "600519"）
        data_type: 数据类型（目前仅支持"行情"）
        start_date: 开始日期（可选，默认一个月前）
        end_date: 结束日期（可选，默认今天）
    """
    if data_type != "行情":
        raise ValueError("目前仅支持'行情'数据类型")

    # 设置默认时间范围（最近一个月）
    if not end_date:
        end_date = datetime.now().strftime("%Y%m%d")
    if not start_date:
        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y%m%d")

    # 构造请求URL
    url = f"http://push2his.eastmoney.com/api/qt/stock/kline/get?" \
          f"secid=1.{stock_code}&" \
          f"fields1=f1,f2,f3,f4,f5,f6&" \
          f"fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61&" \
          f"klt=101&fqt=1&" \
          f"beg={start_date}&end={end_date}"

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        klines = res.json()['data']['klines']

        df = pd.DataFrame([line.split(',') for line in klines], columns=[
            "date", "open", "close", "high", "low", "volume",
            "amount", "amplitude", "change_pct", "change_amt", "turnover"
        ])
        return df

    except Exception as e:
        raise ValueError(f"数据获取失败: {str(e)}")
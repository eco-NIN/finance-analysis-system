# @Author  : eco
# @Date    :2025/6/7 16:19
# @Function:
# app/services/prediction/extractor.py
import json

import requests
import pandas as pd
from app.models.prediction import RawData

def fetch_dongfang_data(stock_code: str, data_type: str) -> pd.DataFrame:
    """
    从东方财富网获取股票的历史行情或财务数据。
    """
    if data_type == "行情":
        url = f"http://push2his.eastmoney.com/api/qt/stock/kline/get?secid=1.{stock_code}&fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61&klt=101&fqt=1&beg=20220101&end=20240601"
        res = requests.get(url)
        klines = res.json()['data']['klines']
        df = pd.DataFrame([line.split(',') for line in klines], columns=[
            "date", "open", "close", "high", "low", "volume", "amount", "amplitude", "change_pct", "change_amt", "turnover"
        ])
        return df
    else:
        raise ValueError("不支持的数据类型")


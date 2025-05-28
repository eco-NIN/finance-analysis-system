import tushare as ts
import pandas as pd
import time

def fetch_stock_data(stock_code: str, start_date: str, end_date: str) -> pd.DataFrame:
    ts.set_token("767826689a4921b691851a85348d23dfefef26dfda6abcf7de01bf53")
    pro = ts.pro_api()
    for _ in range(3):  # 最多尝试3次
        try:
            df = pro.daily(ts_code=stock_code, start_date=start_date.replace("-", ""), end_date=end_date.replace("-", ""))
            if df is not None and not df.empty:
                # print("成功拉取的前10条数据：")
                # print(df.head(10))  # ✅ 输出前10条
                return df
        except Exception as e:
            print("拉取数据失败，重试中：", e)
            time.sleep(1)
    raise RuntimeError("拉取股票数据失败")
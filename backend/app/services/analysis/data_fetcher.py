import tushare as ts
import pandas as pd

def fetch_stock_data(stock_code: str, start_date: str, end_date: str) -> pd.DataFrame:
    ts.set_token("767826689a4921b691851a85348d23dfefef26dfda6abcf7de01bf53")
    pro = ts.pro_api()
    df = pro.daily(ts_code=stock_code, start_date=start_date.replace("-", ""), end_date=end_date.replace("-", ""))
    return df

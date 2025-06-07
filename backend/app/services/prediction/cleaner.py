# @Author  : eco
# @Date    :2025/6/7 16:19
# @Function:
# app/services/prediction/cleaner.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna()
    df['close'] = pd.to_numeric(df['close'])
    df['open'] = pd.to_numeric(df['open'])
    df['change_pct'] = pd.to_numeric(df['change_pct'])
    return df[['date','open', 'close', 'change_pct']]
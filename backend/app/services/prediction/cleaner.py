# @Author  : eco
# @Date    :2025/6/7 16:19
# @Function:
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    清洗并增强股票数据，生成适用于各类模型的特征
    返回字段说明：
    - 基础字段: date, open, close, high, low, volume
    - 衍生特征: change_pct, ma_5, ma_10, volatility
    - 分类标签: target (1表示次日上涨，0表示下跌)
    """
    df = df.copy()

    # 1. 类型转换和去空
    numeric_cols = ['open', 'close', 'high', 'low', 'volume', 'amount']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    df = df.dropna()

    # 2. 基础特征保留
    keep_cols = ['date', 'open', 'close', 'high', 'low', 'volume']
    df = df[keep_cols]

    # 3. 添加衍生特征（增强模型表现）
    df = add_technical_indicators(df)

    return df


def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """添加技术指标特征"""
    # 涨跌幅
    df['change_pct'] = (df['close'] - df['open']) / df['open'] * 100

    # 移动平均线
    df['ma_5'] = df['close'].rolling(5).mean()  # 5日均线
    df['ma_10'] = df['close'].rolling(10).mean()  # 10日均线

    # 波动率（标准差）
    df['volatility'] = df['close'].rolling(5).std()

    # 次日涨跌标签（用于分类任务）
    df['target'] = (df['close'].shift(-1) > df['close']).astype(int)

    # 删除因滚动计算产生的空值
    df = df.dropna()

    return df
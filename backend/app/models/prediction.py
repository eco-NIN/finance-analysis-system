# @Author  :郭宇哲
# @Date    :2025/6/7 16:34
# @Function:东方财富爬虫原始数据+清洗数据+预测数据
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from app.models.base import Base
from sqlalchemy.dialects.mysql import LONGTEXT

class RawData(Base):
    __tablename__ = "raw_data"

    id = Column(Integer, primary_key=True, index=True)
    stock_code = Column(String(20), index=True)
    # raw_json = Column(String(10000))  # 原始网页数据（或json结构）
    raw_json = Column(LONGTEXT)  # 原始网页数据（或json结构）

class CleanData(Base):
    __tablename__ = "clean_data"

    id = Column(Integer, primary_key=True, index=True)
    stock_code = Column(String(20), index=True)  # 股票代码
    date = Column(String(20))  # 日期

    # 基础行情数据
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)  # 新增
    low = Column(Float)  # 新增
    volume = Column(Float)  # 新增

    # 技术指标
    change_pct = Column(Float)  # 涨跌幅
    ma_5 = Column(Float)  # 5日均线（新增）
    ma_10 = Column(Float)  # 10日均线（新增）
    volatility = Column(Float)  # 波动率（新增）

    created_at = Column(DateTime)  # 创建时间

class PredictionResult(Base):
    __tablename__ = "prediction_results"

    id = Column(Integer, primary_key=True)
    stock_code = Column(String(20))        # 股票代码一般不超过20位
    task_type = Column(String(20))         # 回归/分类
    algorithm = Column(String(50))         # 算法名（如XGBoost、LSTM等）
    prediction = Column(JSON)
    metric_name = Column(String(50))       # mse/accuracy等
    metric_value = Column(Float)
    created_at = Column(DateTime)

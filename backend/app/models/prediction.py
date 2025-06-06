# @Author  : eco
# @Date    :2025/6/7 16:34
# @Function:
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
# from .base import Base
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
    stock_code = Column(String(20), index=True)
    date = Column(String(20))
    open = Column(Float)
    close = Column(Float)
    change_pct = Column(Float)

class PredictionResult(Base):
    __tablename__ = "prediction_result"

    id = Column(Integer, primary_key=True, index=True)
    stock_code = Column(String(20), index=True)
    prediction = Column(String(1000))  # JSON 序列化后的预测数组
    mse = Column(Float)
    created_at = Column(DateTime)


# class PredictionResult(Base):
#     __tablename__ = "prediction_results"
#
#     id = Column(Integer, primary_key=True, index=True)
#     stock_code = Column(String(20))
#     data_type = Column(String(20))
#     algorithm = Column(String(20))
#     prediction = Column(JSON)
#     metrics = Column(JSON)

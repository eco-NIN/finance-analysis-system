# @Author  : eco
# @Date    :2025/5/22 09:54
# @Function: 定义金融数据模型
# app/models/stock.py

from sqlalchemy import Column, String, Float, Integer
# from app.core.database import Base
from app.models.base import Base

class StockBasic(Base):
    __tablename__ = "stock_basic"

    ts_code = Column(String(20), primary_key=True, index=True)
    name = Column(String(50))
    area = Column(String(50))
    industry = Column(String(50))
    market = Column(String(50))

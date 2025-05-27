# @Author  : eco
# @Date    :2025/5/21 21:26
# @Function:数据爬虫模块测试路由，仅负责请求参数验证和路由注册

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.stock import StockBasic
import tushare as ts
import pandas as pd
from app.services.crawler.crawler_service import fetch_and_store_stock_basic

router = APIRouter()
@router.get("/test")
def test_crawler():
    return {"message": "Crawler module works!"}
# 设置 Tushare token
ts.set_token('f0bf7c7973cb2dc826382015efc4f6a0d2733fff14aa50aa5d14a4ed')
pro = ts.pro_api()


@router.get("/fetch_stock_basic",summary="抓取tushare数据测试")
def fetch_stock_basic(db: Session = Depends(get_db)):
    """
    获取基础股票信息，并存入数据库
    """
    count = fetch_and_store_stock_basic(db)
    data = db.query(StockBasic).limit(100).all()  # 可分页、只取前100条
    return {
        "message": f"{count} stocks saved to DB",
        "data": data
    }

@router.get("/stock_list", summary="获取已保存的股票信息")
def get_saved_stock_basic(db: Session = Depends(get_db)):
    """
    从数据库中读取已保存的股票基本信息
    """
    stocks = db.query(StockBasic).limit(100).all()  # 根据你的模型名改动
    return {"data": [stock.__dict__ for stock in stocks]}


# @router.get("/stock_list", summary="读取数据库中已保存的股票基本信息")
# def get_saved_stock_basic(db: Session = Depends(get_db)):
#     stocks = db.query(StockBasic).limit(100).all()
#     return {"data": [  # 只返回几个字段用于前端展示
#         {
#             "ts_code": stock.ts_code,
#             "name": stock.name,
#             "area": stock.area,
#             "industry": stock.industry,
#             "list_date": stock.list_date
#         } for stock in stocks
#     ]}
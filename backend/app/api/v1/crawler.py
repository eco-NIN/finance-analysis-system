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


@router.get("/fetch_stock_basic")
def fetch_stock_basic(db: Session = Depends(get_db)):
    """
    获取基础股票信息，并存入数据库
    """
    count = fetch_and_store_stock_basic(db)
    return {"message": f"{count} stocks saved to DB"}
# @Author  : eco
# @Date    :2025/5/22 10:42
# @Function:
import tushare as ts
from sqlalchemy.orm import Session
from app.models.stock import StockBasic

# 设置 tushare token（推荐放 config）
ts.set_token('f0bf7c7973cb2dc826382015efc4f6a0d2733fff14aa50aa5d14a4ed')
pro = ts.pro_api()

def fetch_and_store_stock_basic(db: Session) -> int:
    df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name,area,industry,market')
    for _, row in df.iterrows():
        stock = StockBasic(
            ts_code=row.ts_code,
            name=row.name,
            area=row.area,
            industry=row.industry,
            market=row.market
        )
        db.merge(stock)
    db.commit()
    return len(df)
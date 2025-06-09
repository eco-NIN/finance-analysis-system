# @Author  :郭宇哲
# @Date    :2025/5/21 21:25
# @Function:FastAPI 中用来接收和验证前端传参的核心机制，定义了一个数据模型类，用于描述接口需要接收的数据结构。
from pydantic import BaseModel
from typing import List, Dict

# 以下是tushare的数据模型
class PredictRequest(BaseModel):
    ts_code: str
    start_date: str
    end_date: str

# 以下是东方财富的数据模型
class PredictionRequest(BaseModel):
    stock_code: str
    data_type: str   # e.g. "行情"
    algorithm: str   # "回归" or "分类"

class RawData(BaseModel):
    date: str
    open: float
    close: float
    high: float
    low: float
    volume: float
    amount: float
    amplitude: float
    change_pct: float
    change_amt: float
    turnover: float

class CleanData(BaseModel):
    date: str
    open: float
    close: float
    change_pct: float

class PredictionResponse(BaseModel):
    stock_code: str
    raw_data: List[RawData]
    clean_data: List[CleanData]
    prediction: List[float]
    metrics: Dict[str, float]
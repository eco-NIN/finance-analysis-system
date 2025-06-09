# @Author  :郭宇哲
# @Date    :2025/5/21 21:25
# @Function:FastAPI 中用来接收和验证前端传参的核心机制，定义了一个数据模型类，用于描述接口需要接收的数据结构。
from pydantic import BaseModel
from typing import Literal


# 以下是tushare的数据模型
class PredictRequest(BaseModel):
    ts_code: str
    start_date: str
    end_date: str

# 以下是东方财富的数据模型
class PredictionRequest(BaseModel):
    stock_code: str
    # data_type: str   # e.g. "行情"
    # algorithm: str   # "回归" or "分类"
    data_type: Literal["行情"]  # 目前仅支持行情数据
    task_type: Literal["回归", "分类"]  # 新增：任务类型
    algorithm: str  # 示例: "线性回归"、"随机森林"、"逻辑回归"、"支持向量机"
    start_date: str = None  # 新增
    end_date: str = None    # 新增

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
    high: float  # 新增
    low: float  # 新增
    volume: float  # 新增
    change_pct: float
    ma_5: float  # 新增
    ma_10: float  # 新增
    volatility: float  # 新增

    class Config:
        orm_mode = True  # 允许从ORM模型自动转换

class PredictionResponse(BaseModel):
    stock_code: str
    task_type: str  # 新增
    algorithm: str  # 新增
    raw_data: list[dict]  # DataFrame.to_dict("records") 的结果
    clean_data: list[dict]
    prediction: list
    metrics: dict  # 可能包含 "mse" 或 "accuracy"
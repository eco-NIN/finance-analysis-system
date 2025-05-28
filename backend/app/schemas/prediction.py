# @Author  : eco
# @Date    :2025/5/21 21:25
# @Function:FastAPI 中用来接收和验证前端传参的核心机制，它定义了一个数据模型类，用于描述接口需要接收的数据结构。

from pydantic import BaseModel

class PredictRequest(BaseModel):
    ts_code: str
    start_date: str
    end_date: str
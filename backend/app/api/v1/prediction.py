# @Author  : eco
# @Date    :2025/5/21 21:26
# @Function:机器学习预测模块测试路由
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_prediction():
    return {"message": "Prediction module works!"}
# @Author  : eco
# @Date    :2025/5/21 21:26
# @Function:金融分析模块测试路由
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_analysis():
    return {"message": "Analysis module works!"}
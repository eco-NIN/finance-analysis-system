# @Author  : eco
# @Date    :2025/5/21 21:26
# @Function:机器学习预测模块测试路由
from fastapi import APIRouter, HTTPException
from app.services.analysis.data_fetcher import fetch_stock_data  # 复用已有分析模块
from app.services.prediction.predict_model import run_predictions
from app.schemas.prediction import PredictRequest

router = APIRouter()

@router.get("/test")
def test_prediction():
    return {"message": "Prediction module works!"}



@router.post("/predict")
def predict_stock(req: PredictRequest):
    try:
        df = fetch_stock_data(req.ts_code, req.start_date, req.end_date)
        result = run_predictions(df)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
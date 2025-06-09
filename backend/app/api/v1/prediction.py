# @Author  : eco
# @Date    :2025/5/21 21:26
# @Function:机器学习预测模块测试路由
from fastapi import APIRouter, HTTPException
from app.services.prediction.extractor import fetch_dongfang_data
from app.services.prediction.cleaner import clean_data
from app.services.prediction.trainer import train_and_predict
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.models.prediction import PredictionResult
from app.core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.services.prediction.entry import run_prediction_pipeline
from app.services.prediction.tushare_predict import run_predictions
from app.schemas.prediction import PredictRequest
from app.services.analysis.data_fetcher import fetch_stock_data # 复用已有分析模块

router = APIRouter()


@router.post("/tushare_predict")
def predict_stock(req: PredictRequest):
    try:
        df = fetch_stock_data(req.ts_code, req.start_date, req.end_date)
        result = run_predictions(df)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest, db: Session = Depends(get_db)):
    return run_prediction_pipeline(request, db)

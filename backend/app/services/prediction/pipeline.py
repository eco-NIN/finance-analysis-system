# @Author  : eco
# @Date    :2025/6/7 17:01
# @Function:总接口
# app/services/prediction/pipeline.py
import json
from datetime import datetime
from sqlalchemy.orm import Session

from app.services.prediction.extractor import fetch_dongfang_data
from app.services.prediction.cleaner import clean_data
from app.services.prediction.trainer import train_and_predict
from app.services.prediction.storage import store_raw_data, store_clean_data, store_prediction_result

from app.schemas.prediction import PredictionRequest,PredictionResponse


def run_prediction_pipeline(request: PredictionRequest, db: Session):
    # 1. 爬虫获取数据
    raw_data = fetch_dongfang_data(request.stock_code, request.data_type)
    store_raw_data(db, request, raw_data)

    # 2. 清洗数据
    cleaned_data = clean_data(raw_data)
    store_clean_data(db, request, cleaned_data)

    # 3. 模型预测,存储预测结果
    results = train_and_predict(cleaned_data, request.algorithm)
    store_prediction_result(db, request, results)

    # 5. 返回结果
    # return {
    #     "stock_code": request.stock_code,
    #     "prediction": results["prediction"],
    #     "metrics": results["metrics"]
    # }
    # 更加安全

    # 两个数据 raw_data 和 cleaned_data 都是 Pandas 的 DataFrame，
    # 不能直接传给 Pydantic 的模型字段，它们期望的是字典列表（List[Dict]），
    # 或者对应的数据模型列表。

    return PredictionResponse(
        stock_code=request.stock_code,
        raw_data=raw_data.to_dict(orient='records'),
        clean_data=cleaned_data.to_dict(orient='records'),
        prediction=results["prediction"],
        metrics=results["metrics"]
    )
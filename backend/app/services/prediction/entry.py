# @Author  : eco
# @Date    :2025/6/7 17:01
# @Function:总接口

from typing import Dict, Any
import pandas as pd
from sqlalchemy.orm import Session
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction.extractor import fetch_dongfang_data
from app.services.prediction.cleaner import clean_data
from app.services.prediction.trainer import train_and_predict
from app.services.prediction.storage import store_raw_data, store_clean_data, store_prediction_result

def run_prediction_pipeline(
        request: PredictionRequest,
        db: Session
) -> PredictionResponse:
    """
    完整的预测流水线：
    1. 爬取数据 -> 2. 清洗数据 -> 3. 训练模型 -> 4. 存储结果 -> 5. 返回响应
    """
    # 1. 爬取原始数据
    raw_data = fetch_dongfang_data(request.stock_code, request.data_type,request.start_date,request.end_date)
    store_raw_data(db, request, raw_data)  # 存储原始数据

    # 2. 数据清洗
    cleaned_data = clean_data(raw_data)
    store_clean_data(db, request, cleaned_data)  # 存储清洗后数据

    # 3. 模型训练与预测（适配新的4种模型）
    results = train_and_predict(
        df=cleaned_data,
        task_type=request.task_type,  # 新增参数：任务类型（回归/分类）
        algorithm=request.algorithm  # 新增参数：具体算法
    )
    store_prediction_result(db, request, results)  # 存储预测结果

    # 4. 构造响应（适配DataFrame转字典）
    return PredictionResponse(
        stock_code=request.stock_code,
        task_type=request.task_type,  # 新增字段
        algorithm=request.algorithm,  # 新增字段
        raw_data=raw_data.to_dict(orient="records"),
        clean_data=cleaned_data.to_dict(orient="records"),
        prediction=results["prediction"],
        metrics=results["metrics"]
    )
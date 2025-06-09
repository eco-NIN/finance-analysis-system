# @Author  : eco
# @Date    :2025/6/7 17:03
# @Function:
# app/services/prediction/storage.py
from sqlalchemy.orm import Session
import json
from datetime import datetime
import pandas as pd
from app.models.prediction import RawData, CleanData
from app.models.prediction import PredictionResult
from app.schemas.prediction import PredictionRequest

def store_raw_data(db: Session, request: PredictionRequest, raw_data: pd.DataFrame):
    raw_json = raw_data.to_dict(orient="records")  # 转为 list[dict]
    db.add(RawData(
        stock_code=request.stock_code,
        raw_json=json.dumps(raw_json)  # 转为 JSON 字符串
    ))
    # 报错---需要将DataFrame 转换为原生 Python 数据结构，再进行序列化：
    # db.add(RawData(
    #     stock_code=request.stock_code,
    #     raw_json=json.dumps(raw_data)  # 爬取后未清洗的数据
    # ))
    db.commit()

def store_clean_data(db: Session, request: PredictionRequest, cleaned_data: pd.DataFrame):
    for _, row in cleaned_data.iterrows():
        exists = db.query(CleanData).filter(
            CleanData.stock_code == request.stock_code,
            CleanData.date == row["date"]
        ).first()
        if not exists:
            db.add(CleanData(
                stock_code=request.stock_code,
                date=row["date"],
                open=row["open"],
                close=row["close"],
                high=row["high"],          # 新增
                low=row["low"],            # 新增
                volume=row["volume"],      # 新增
                change_pct=row["change_pct"],
                ma_5=row["ma_5"],         # 新增
                ma_10=row["ma_10"],       # 新增
                volatility=row["volatility"],  # 新增
                created_at=datetime.now()
            ))
    db.commit()

def store_prediction_result(db: Session, request: PredictionRequest, result: dict):
    """
    存储预测结果（适配回归和分类任务）
    """
    # 根据任务类型选择存储的评估指标
    if request.task_type == "回归":
        metric_name = "mse"
        metric_value = result["metrics"]["mse"]
    else:  # 分类任务
        metric_name = "accuracy"
        metric_value = result["metrics"]["accuracy"]

    db.add(PredictionResult(
        stock_code=request.stock_code,
        task_type=request.task_type,      # 新增字段：任务类型
        algorithm=request.algorithm,      # 新增字段：算法名称
        prediction=json.dumps(result["prediction"]),
        metric_name=metric_name,          # 动态存储指标名称
        metric_value=metric_value,        # 动态存储指标值
        created_at=datetime.now()
    ))
    db.commit()
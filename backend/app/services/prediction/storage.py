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
                change_pct=row["change_pct"]
            ))
    db.commit()

    # db.add(CleanData(
    #     stock_code=request.stock_code,
    #     data_type=request.data_type,
    #     content=json.dumps(cleaned_data.to_dict(orient="records")),
    #     created_at=datetime.now()
    # ))


def store_prediction_result(db: Session, request: PredictionRequest, result: dict):
    db.add(PredictionResult(
        stock_code=request.stock_code,
        prediction=json.dumps(result["prediction"]),
        mse=result["metrics"]["mse"],
        created_at=datetime.now()
    ))
    db.commit()
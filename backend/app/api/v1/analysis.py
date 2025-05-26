from fastapi import APIRouter, Query
from app.services.analysis.analyzer import analyze_stock_data

router = APIRouter()

@router.get("/analyze")
def analyze(
    stock_code: str = Query(..., description="股票代码"),
    start_date: str = Query(..., description="开始日期"),
    end_date: str = Query(..., description="结束日期")
):
    result_data, image_base64 = analyze_stock_data(stock_code, start_date, end_date)
    return {
        "result": result_data,
        "image_base64": image_base64
    }


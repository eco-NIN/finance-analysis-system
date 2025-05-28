from fastapi import APIRouter, Query
from app.services.analysis.analyzer import analyze_stock_data

router = APIRouter()

@router.get("/analyze")
def analyze(
    ts_code: str = Query(..., description="股票代码"),
    start_date: str = Query(..., description="开始日期"),
    end_date: str = Query(..., description="结束日期")
):
    result_data, image_base64_1,image_base64_2,image_base64_3,image_base64_4 = analyze_stock_data(ts_code, start_date, end_date)
    return {
        "result": result_data,
        "image_base64_1": image_base64_1,
        "image_base64_2": image_base64_2,
        "image_base64_3": image_base64_3,
        "image_base64_4": image_base64_4
    }


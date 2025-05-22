# @Author  : eco
# @Date    :2025/5/21 20:47
# @Function:

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from core.config import settings
# from core.database import engine, Base
from app.api.v1 import crawler, analysis, prediction#, file

# 创建数据库表（如果没有的话）
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="金融数据分析平台",
    description="基于 FastAPI 的金融数据分析 + 文献处理 + 机器学习预测系统",
    version="1.0.0"
)

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或配置指定前端地址，例如 "http://localhost:5173"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 路由挂载
app.include_router(crawler.router, prefix="/api/v1/crawler", tags=["数据爬虫"])
app.include_router(analysis.router, prefix="/api/v1/analysis", tags=["金融分析"])
app.include_router(prediction.router, prefix="/api/v1/prediction", tags=["机器学习预测"])
# app.include_router(file.router, prefix="/api/v1/file", tags=["文件处理"])
# 健康检查
@app.get("/ping", tags=["系统"])
def ping():
    return {"message": "pong"}

from app.api.v1 import crawler

app.include_router(crawler.router, prefix="/api/v1/crawler", tags=["抓取tushare数据测试"])
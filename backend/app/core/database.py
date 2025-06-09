# @Author  : eco
# @Date    :2025/5/21 21:24
# @Function: 数据库连接与 ORM 初始化,数据库连接管理（SQLAlchemy + 会话）
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base  # 从 models/base.py 引入 Base
from app.core.config import settings

# 创建数据库引擎（使用 DATABASE_URL）
engine = create_engine(settings.database_url, pool_pre_ping=True)
# 创建 SessionLocal，每次请求都会用这个类创建 session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# FastAPI 依赖注入：获取数据库 session 的函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
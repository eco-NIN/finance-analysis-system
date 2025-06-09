# @Author  :郭宇哲
# @Date    :2025/5/21 21:24
# @Function:ORM 基类（可供其他模型继承），定义数据模型
from sqlalchemy.orm import declarative_base

Base = declarative_base()
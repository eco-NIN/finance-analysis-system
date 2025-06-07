# @Author  : eco
# @Date    :2025/5/21 20:48
# @Function:
# 初始化数据库（仅首次） 指的是执行
# Base.metadata.create_all(bind=engine)
# 来在数据库中创建你定义的表结构。这个操作一般我们单独放在一个脚本文件中，而不是放在
# main.py
# 里，避免每次启动都重复创建表。


from app.core.database import Base, engine
from app.models import stock  # 确保导入模型
from app.models import prediction

def init():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("All tables created.")

if __name__ == "__main__":
    init()
# @Author  :郭宇哲
# @Date    :2025/5/21 20:48
# @Function:初始化本地数据库
from app.core.database import Base, engine

def init():
    print("Creating tables...")
    # 在数据库中创建定义的表结构，之所以单独放在一个脚本文件中，而不是放在main.py里，是为了避免每次启动都重复创建表
    Base.metadata.create_all(bind=engine)
    print("All tables created.")

if __name__ == "__main__":
    init()
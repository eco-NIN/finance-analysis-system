# @Author  : eco
# @Date    :2025/6/7 16:20
# @Function:
# app/services/prediction/trainer.py
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
import pandas as pd

def train_and_predict(df: pd.DataFrame, task_type: str,algorithm: str):
    model = None  # 显式初始化
    """
    参数:
        task_type: "回归" 或 "分类"
        algorithm:
            - 回归任务下可选: "线性回归" 或 "随机森林"
            - 分类任务下可选: "逻辑回归" 或 "支持向量机"
    """
    # # 准备数据
    # X = df[['open']]
    # if task_type == "回归":
    #     y = df['close']
    # else:  # 分类
    #     y = (df['change_pct'] > 0).astype(int)  # 涨为1，跌为0

    # 回归任务使用所有特征
    if task_type == "回归":
        X = df[['open', 'high', 'low', 'volume', 'ma_5', 'ma_10', 'volatility']]
        y = df['close']

    # 分类任务需排除close（因为target是基于close计算的）
    else:
        X = df[['open', 'high', 'low', 'volume', 'ma_5', 'ma_10', 'volatility']]
        y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)


    # 训练模型
    if task_type == "回归":
        if algorithm == "线性回归":
            model = LinearRegression()
        elif algorithm == "随机森林":
            model = RandomForestRegressor(n_estimators=100)
        if model is None:
            raise ValueError(f"不支持的算法组合: task_type={task_type}, algorithm={algorithm}")

        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        mse = mean_squared_error(y_test, prediction)
        return {
            "task_type": task_type,
            "algorithm": algorithm,
            "prediction": prediction.tolist()[:5],  # 返回前5个预测结果示例
            "metrics": {"mse": mse}
        }
    else:  # 分类
        if algorithm == "逻辑回归":
            model = LogisticRegression()
        elif algorithm == "支持向量机":
            model = SVC(probability=True)
        if model is None:
            raise ValueError(f"不支持的算法组合: task_type={task_type}, algorithm={algorithm}")

        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        acc = accuracy_score(y_test, prediction)


        return {
            "task_type": task_type,
            "algorithm": algorithm,
            "prediction": prediction.tolist()[:5],
            "metrics": {"accuracy": acc}
        }
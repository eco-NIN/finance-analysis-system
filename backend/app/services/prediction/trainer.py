# @Author  : eco
# @Date    :2025/6/7 16:20
# @Function:
# app/services/prediction/trainer.py
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
import numpy as np
import pandas as pd

def train_and_predict(df: pd.DataFrame, algorithm: str):
    X = df[['open']]
    y = df['close'] if algorithm == "回归" else (df['change_pct'] > 0).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    if algorithm == "回归":
        model = LinearRegression()
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        mse = mean_squared_error(y_test, prediction)
        return {
            "prediction": prediction.tolist()[:5],
            "metrics": {"mse": mse}
        }
    else:
        model = LogisticRegression()
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        acc = accuracy_score(y_test, prediction)
        return {
            "prediction": prediction.tolist()[:5],
            "metrics": {"accuracy": acc}
        }
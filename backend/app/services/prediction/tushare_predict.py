# @Author  : eco
# @Date    :2025/5/28 17:21
# @Function: 模型训练和预测逻辑
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

def run_predictions(df: pd.DataFrame):
    df = df.sort_values(by='trade_date')
    df['label_reg'] = df['close'].shift(-1)   # 回归目标：下一日收盘价
    df['label_cls'] = (df['pct_chg'].shift(-1) > 0).astype(int)  # 分类目标：下一日是否上涨

    df.dropna(inplace=True)

    features = ['open', 'high', 'low', 'close', 'vol', 'amount']
    X = df[features]
    y_reg = df['label_reg']
    y_cls = df['label_cls']

    X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
    _, _, y_train_cls, y_test_cls = train_test_split(X, y_cls, test_size=0.2, random_state=42)

    # 模型训练
    lr = LinearRegression().fit(X_train, y_train_reg)
    rf = RandomForestRegressor().fit(X_train, y_train_reg)
    log_reg = LogisticRegression(max_iter=1000).fit(X_train, y_train_cls)
    svm = SVC().fit(X_train, y_train_cls)

    # 预测：对最新的一条数据做预测（通常是最后一天）
    latest_data = df[features].iloc[[-1]]  # 2D 结构

    predicted_close_lr = lr.predict(latest_data)[0]
    predicted_close_rf = rf.predict(latest_data)[0]
    predicted_up_log = log_reg.predict(latest_data)[0]
    predicted_up_svm = svm.predict(latest_data)[0]

    return {
        "回归模型评估": {
            "线性回归": {
                "MSE": mean_squared_error(y_test_reg, lr.predict(X_test)),
                "R2": r2_score(y_test_reg, lr.predict(X_test))
            },
            "随机森林回归": {
                "MSE": mean_squared_error(y_test_reg, rf.predict(X_test)),
                "R2": r2_score(y_test_reg, rf.predict(X_test))
            }
        },
        "分类模型评估": {
            "逻辑回归": {
                "准确率": accuracy_score(y_test_cls, log_reg.predict(X_test))
            },
            "支持向量机": {
                "准确率": accuracy_score(y_test_cls, svm.predict(X_test))
            }
        },
        "最新预测": {
            "下一日收盘价预测（线性回归）": predicted_close_lr,
            "下一日收盘价预测（随机森林）": predicted_close_rf,
            "下一日是否上涨预测（逻辑回归）": "上涨" if predicted_up_log == 1 else "下跌",
            "下一日是否上涨预测（SVM）": "上涨" if predicted_up_svm == 1 else "下跌"
        }
    }
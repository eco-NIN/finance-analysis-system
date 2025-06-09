# 📊 金融分析系统

基于 **FastAPI + Vue3 + Element Plus** 的金融数据处理平台，实现以下功能：

- 🕸️ 数据爬虫（实时抓取金融数据）
- 📈 金融图像分析（清洗、可视化、导出）
- 🤖 机器学习预测（模型训练与预测展示）

---
### 前端页面
![img.png](docs/img_1.png)
![img.png](docs/img_2.png)
![img_3.png](docs/img_3.png)
![img_4.png](docs/img_4.png)
![img_5.png](docs/img_5.png)
![img_6.png](docs/img_6.png)
![img_7.png](docs/img_7.png)
### 后端接口页面
![img_8.png](docs/img_8.png)
---

## 🧰 技术栈

| 后端       | FastAPI · SQLAlchemy · MySQL |
| ---------- | ----------------------------- |
| 前端       | Vue3 · Vite · Pinia · Element Plus |
| 其他       | Axios · ECharts · Pydantic |

---

## 🚀 快速启动

```bash
# 克隆项目
git clone https://github.com/eco-NIN/finance-analysis-system.git
cd finance-analysis-system
```

## 启动前端
```bash
cd frontend
npm install
npm run dev
```
## 启动后端


```bash
cd backend
python -m venv venv         # 或 conda create --name faenv python=3.10
source venv/bin/activate #windows venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
## 在backend中配置后端数据库.env 
```angular2html
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=root
DATABASE_PASSWORD=12345678
DATABASE_NAME=finance
DATABASE_URL=mysql+pymysql://root:12345678@localhost:3306/finance
```
## 初始化本地数据库
```python
# 运行以下文件
# backend/initial_data.py
```

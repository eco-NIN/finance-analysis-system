# 📊 金融分析系统

基于 **FastAPI + Vue3 + Element Plus** 的金融数据处理平台，实现以下功能：

- 🕸️ 数据爬虫模块（实时抓取金融数据）
- 📈 金融分析模块（清洗、可视化、导出）
- 🤖 机器学习预测模块（模型训练与预测展示）

---
### 前端页面
![img1.png](docs/img1.png)
### 后端接口页面
![img.png](docs/img.png)
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
git clone https://github.com/your-org/finance-analysis-system.git
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
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

> 不用看
> 
> npm init vite@latest frontend

## 配置后端数据库.env 在backend中
```angular2html
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=root
DATABASE_PASSWORD=12345678
DATABASE_NAME=finance
DATABASE_URL=mysql+pymysql://root:12345678@localhost:3306/finance
```


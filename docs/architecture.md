                          ┌────────────┐
                          │  用户界面   │   ← 前端（框架待定）
                          └────┬───────┘
                               │HTTP (RESTful / WebSocket)
                               ▼
                         ┌────────────┐
                         │  FastAPI后端 │
                         └────┬───────┘
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
 ┌────────────┐      ┌────────────────┐    ┌────────────────┐
 │ 数据爬虫模块 │      │ 金融分析模块   │    │ 机器学习预测模块 │
 └────┬───────┘      └────────────────┘    └────────────────┘
      ▼                                           ▲
 ┌────────────┐                         ┌────────────────┐
 │ 爬取的数据  │                         │ 处理/预测结果   │
 └────┬───────┘                         └────┬────────────┘
      ▼                                        ▼
 ┌────────────┐                         ┌────────────┐
 │ MySQL数据库 │←保存/读取→(结果)         │ 文件系统   │←保存图表/CSV等
 └────────────┘                         └────────────┘
 

finance-analysis-system/
│
├── backend/                    # FastAPI 后端
│   ├── app/
│   │   ├── api/                # 路由层（API接口）
│   │   │   ├── v1/
│   │   │   │   ├── crawler.py
│   │   │   │   ├── analysis.py
│   │   │   │   ├── prediction.py
│   │   │   │   └── file.py
│   │   │   └── deps.py         # 依赖注入（如 DB）
│   │   │
│   │   ├── services/           # 业务逻辑层
│   │   │   ├── crawler/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── extractor.py
│   │   │   │   └── parser.py
│   │   │   ├── analysis/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── cleaner.py
│   │   │   │   ├── visualizer.py
│   │   │   │   └── exporter.py
│   │   │   ├── prediction/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── trainer.py
│   │   │   │   ├── models.py
│   │   │   │   └── evaluator.py
│   │   │   └── common/
│   │   │       ├── file_utils.py
│   │   │       └── data_utils.py
│   │   │
│   │   ├── core/               # 核心配置（应用启动、配置、数据库）
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   ├── logger.py
│   │   │   └── security.py     # 如果有鉴权
│   │   │
│   │   ├── models/             # ORM模型
│   │   │   ├── base.py
│   │   │   ├── financial_data.py
│   │   │   ├── analysis_result.py
│   │   │   └── prediction_result.py
│   │   │
│   │   ├── schemas/            # Pydantic 模型
│   │   │   ├── crawler.py
│   │   │   ├── analysis.py
│   │   │   ├── prediction.py
│   │   │   └── file.py
│   │   │
│   │   ├── main.py             # FastAPI 应用主入口
│   │   └── initial_data.py     # 初始化数据库（可选）
│   │
│   └── requirements.txt        # 后端依赖列表
│
├── frontend/                   # Vue3 + Element Plus 前端
│   ├── public/                 # 公共资源
│   ├── src/
│   │   ├── assets/             # 静态资源
│   │   ├── components/         # 可复用组件
│   │   │   ├── DataUploader.vue
│   │   │   ├── ChartRenderer.vue
│   │   │   └── ResultCard.vue
│   │   ├── pages/              # 页面模块
│   │   │   ├── Home.vue
│   │   │   ├── Crawler.vue
│   │   │   ├── Analysis.vue
│   │   │   ├── Prediction.vue
│   │   │   └── History.vue
│   │   ├── router/             # 前端路由
│   │   │   └── index.js
│   │   ├── services/           # 封装的 API 请求
│   │   │   ├── crawler.js
│   │   │   ├── analysis.js
│   │   │   ├── prediction.js
│   │   │   └── file.js
│   │   ├── store/              # 状态管理（使用 pinia）
│   │   │   └── index.js
│   │   ├── App.vue             # 根组件
│   │   └── main.js             # 应用入口
│   ├── vite.config.js
│   └── package.json
│
├── docs/                       # 项目文档
│   ├── api_docs.md
│   ├── architecture.md
│   └── usage_guide.md
│
├── .env                        # 环境变量配置
├── .gitignore
└── README.md

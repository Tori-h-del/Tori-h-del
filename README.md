- 👋 Hi, I’m @Tori-h-del
- 👀 I’m interested in cyber_security
- 🌱 I’m currently learning AI
-      
-# 我的学习博客 - 一个Flask练手项目
&gt; 大二学生做的个人博客，用来记录学习过程。慢慢加功能中，目前能跑就行 😅

**在线演示**: [待部署]  
**技术栈**: Flask + SQLite + Bootstrap

---

## 主要实现
用户注册登录
文章列表和详情页
知识图谱（想做，但还没搞懂）
搜索功能（等文章多了再加）

---
## 项目结构
my_flask_project/
├── app/                  # 核心应用代码目录
│   ├── __init__.py       # 应用工厂 (创建 app 实例的地方)
│   ├── main.py           # 主蓝图 (首页等普通页面)
│   ├── api.py            # API 蓝图 (如果需要前后端分离)
│   ├── templates/        # HTML 模板文件
│   │   └── index.html
│   └── static/           # 静态文件 (CSS, JS, 图片)
│       └── style.css
├── tests/                # 测试代码
├── .env                  # 环境变量 (密钥等，不要上传到 GitHub)
├── requirements.txt      # 依赖列表
└── run.py                # 启动入口


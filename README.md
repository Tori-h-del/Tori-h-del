- 👋 Hi, I’m @Tori-h-del
- 👀 I’m interested in cyber_security
- 🌱 I’m currently learning AI
-      
-# 我的学习博客 - 一个Flask练手项目
&gt; 大三学生做的个人博客，用来记录学习笔记和刷题过程。慢慢加功能中，目前能跑就行 😅

**在线演示**: [待部署]  
**技术栈**: Flask + SQLite + Bootstrap 5

---

## 目前实现了啥

- [x] 用户注册登录（密码用Werkzeug哈希，不算明文存了）
- [x] 发文章（Markdown编辑器，支持代码高亮）
- [x] 文章列表和详情页
- [x] 简单的标签系统
- [x] 学习时长记录（发文章时可选填）
- [ ] 知识图谱（想做，但还没搞懂D3.js）
- [ ] 搜索功能（等文章多了再加）

---
## 项目结构
my-blog/
├── app/
│   ├── init.py          # Flask应用初始化
│   ├── models.py            # 数据库模型（User, Post, Tag）
│   ├── routes.py            # 路由（页面和API）
│   ├── forms.py             # WTForms表单
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── uploads/         # 上传的图片
│   └── templates/
│       ├── base.html        # 基础模板
│       ├── index.html       # 首页
│       ├── login.html
│       ├── register.html
│       ├── create_post.html
│       └── post.html
├── migrations/              # Flask-Migrate生成的
├── tests/                   # 还没写...
├── requirements.txt
├── config.py
└── run.py                   # 启动文件



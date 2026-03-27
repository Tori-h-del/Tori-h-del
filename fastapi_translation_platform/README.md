# 大学生翻译兼职平台（Python Flask 初步框架）

## 核心定位
**翻译兼职 + 志愿时长**：学生拿钱的同时还能拿官方志愿时长，这是其他平台给不了的核心价值。

## 为什么你会遇到 `TemplateNotFound: index.html`
常见原因是：启动命令和当前目录不一致，导致 Flask 在错误目录里找模板。
本项目已经改为**绝对路径加载模板和静态文件**，避免这个问题。

## 1) 安装依赖
```bash
pip install -r requirements.txt
```

## 2) 推荐启动方式（在仓库根目录执行）
```bash
flask --app fastapi_translation_platform.app.app run --debug
```

## 3) 备用启动方式
```bash
python -m fastapi_translation_platform.app.app
```

## 4) 访问地址
- 首页：`http://127.0.0.1:5000/`
- 健康检查：`http://127.0.0.1:5000/health`

## 5) 当前模块（MVP）
- 项目价值主张展示（学生全额拿报酬 + 官方志愿时长）
- 学生端能力展示
- 企业端能力展示
- MVP 模块路线（用户、任务、结算、志愿、评价）

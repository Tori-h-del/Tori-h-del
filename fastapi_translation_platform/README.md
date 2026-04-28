# 大学生翻译兼职平台（Python Flask 初步框架）

## 核心定位
**翻译兼职 + 志愿时长**：学生拿钱的同时还能拿官方志愿时长，这是其他平台给不了的核心价值。

## 你这次报错的原因
你截图里的错误是：
`Could not import 'fastapi_translation_platform.app.app'`

这通常是下面两种情况之一：
1. 命令里模块名拼写错（最常见，`fastapi` / `fastapi` 少字母或多字母）。
2. 启动目录不对，导致 Python 找不到项目包。

## 1) 安装依赖
```bash
pip install -r fastapi_translation_platform/requirements.txt
```

## 2) 最稳妥启动方式（推荐）
在**仓库根目录**执行：
```bash
python run.py
```

## 3) Flask 命令方式（可选）
在**仓库根目录**执行：
```bash
flask --app fastapi_translation_platform.app.app:app run --debug
```

## 4) 访问地址
- 首页：`http://127.0.0.1:5000/`
- 健康检查：`http://127.0.0.1:5000/health`

## 5) 当前模块（MVP）
- 项目价值主张展示（学生全额拿报酬 + 官方志愿时长）
- 学生端能力展示
- 企业端能力展示
- MVP 模块路线（用户、任务、结算、志愿、评价）

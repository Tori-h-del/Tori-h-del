# 大学生翻译平台（FastAPI 初步框架）

## 1) 安装依赖
```bash
pip install -r requirements.txt
```

## 2) 运行项目
```bash
uvicorn app.main:app --reload
```

## 3) 页面与接口
- 首页：`/`
- 健康检查：`/health`
- OpenAPI 文档：`/docs`

## 4) 当前实现（MVP 原型）
- 基于你提供的创业规划书，整理了项目定位、痛点-方案、目标用户、收入结构和功能清单。
- 使用 FastAPI + Jinja2 模板渲染 + CSS 静态样式。
- 便于下一步扩展：登录、任务发布、接单、托管结算、评价与志愿时长模块。

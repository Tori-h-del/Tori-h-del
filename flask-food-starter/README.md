# 新手版 Flask 美食平台（本地 MySQL）

这是一个给初学者的 Flask 练手项目，主题是**美食平台**。
后端使用本地 MySQL，前端只用基础 HTML，不引入 CSS，先专注功能开发。

## 1. 你能学到什么

- Flask 项目最小结构（`app/ + run.py`）
- Blueprint 路由拆分
- Flask-SQLAlchemy 操作 MySQL
- 表单提交（新增菜品 / 新增订单）
- Jinja2 模板渲染
- 最基础 JSON API

## 2. 项目结构

```text
flask-food-starter/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
├── tests/
│   └── test_food_routes.py
├── requirements.txt
├── .env.example
├── .gitignore
└── run.py
```

## 3. 本地 MySQL 准备

先确保本机已安装并启动 MySQL（默认 3306 端口）。

```sql
CREATE DATABASE flask_food_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 4. 如何运行（一步步）

```bash
cd flask-food-starter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

按你的本地 MySQL 改 `.env`：

```env
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=123456
MYSQL_DB=flask_food_demo
```

初始化表和默认菜品：

```bash
flask --app run:app init-db
```

启动项目：

```bash
python run.py
```

浏览器访问：`http://127.0.0.1:5000`

## 5. 页面与 API

- 页面
  - `/` 首页
  - `/dishes` 菜品列表
  - `/dishes/new` 新增菜品
  - `/orders` 订单列表
  - `/orders/new` 新增订单
- API
  - `GET /api/dishes`
  - `GET /api/orders`

## 6. 新手下一步建议

1. 给订单增加总价字段。
2. 增加“删除/编辑菜品和订单”。
3. 增加用户登录和权限。
4. 使用 Flask-Migrate 管理数据库版本。

# Flask 美食平台（无 CSS）

这是一个给初学者的 Flask 练手项目，主题是**美食平台**。
后端保持简单，前端只用基础 HTML，不引入 CSS，方便先把路由、表单、模板和数据流学明白。

## 1. 学到什么

- Flask 项目最小结构（`app/ + run.py`）
- Blueprint 路由拆分
- 表单提交（新增菜品 / 新增订单）
- Jinja2 模板渲染
- 最基础 JSON API
- 内存数据存储（不连数据库，适合入门）

## 2. 项目结构

```text
flask-food-starter/
├── app/
│   ├── __init__.py
│   ├── data.py
│   ├── routes.py
│   └── templates/
│       ├── home.html
│       ├── dishes.html
│       ├── new_dish.html
│       ├── orders.html
│       └── new_order.html
├── tests/
│   └── test_food_routes.py
├── requirements.txt
├── .env.example
├── .gitignore
└── run.py
```

## 3. 快速启动

```bash
cd flask-food-starter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

默认访问：`http://127.0.0.1:5000`

## 4. 页面说明

- `/` 首页导航
- `/dishes` 菜品列表
- `/dishes/new` 新增菜品
- `/orders` 订单列表
- `/orders/new` 新增订单

## 5. API 说明

- `GET /api/dishes`：获取菜品 JSON
- `GET /api/orders`：获取订单 JSON

## 6. 新手下一步建议

1. 把 `app/data.py` 替换成 SQLite（如 Flask-SQLAlchemy）。
2. 给订单增加总价计算。
3. 增加“删除菜品 / 删除订单”功能。
4. 增加登录和权限控制。

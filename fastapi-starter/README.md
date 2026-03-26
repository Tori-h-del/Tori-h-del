# 新手简易版 Python FastAPI 框架

这是一个**入门教学版**的 FastAPI 项目骨架，特点：

- 结构清晰（按 `api / schemas / models / core` 分层）
- 自带健康检查与示例 CRUD 接口
- 内置 pytest 测试样例，方便新手理解接口测试
- 不依赖真实数据库，先用内存假数据层练习

## 1. 项目结构

```text
fastapi-starter/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   └── items.py      # 示例接口
│   │   └── router.py          # 总路由
│   ├── core/
│   │   └── config.py          # 配置管理
│   ├── models/
│   │   └── fake_db.py         # 内存“数据库”
│   ├── schemas/
│   │   └── item.py            # Pydantic 数据模型
│   └── main.py                # FastAPI 应用入口
├── tests/
│   └── test_items.py
├── .env.example
└── requirements.txt
```

## 2. 运行方式

```bash
cd fastapi-starter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

启动后访问：

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- 健康检查: `http://127.0.0.1:8000/health`

## 3. 示例接口

### 创建物品

`POST /api/v1/items`

```json
{
  "name": "键盘",
  "description": "机械键盘"
}
```

### 获取全部物品

`GET /api/v1/items`

### 按 ID 获取物品

`GET /api/v1/items/{item_id}`

## 4. 运行测试

```bash
pytest -q
```

## 5. 新手下一步建议

1. 把 `fake_db.py` 替换成 SQLAlchemy + SQLite。
2. 给接口加分页、搜索参数。
3. 增加用户登录（JWT）。
4. 增加错误码规范与统一异常处理。

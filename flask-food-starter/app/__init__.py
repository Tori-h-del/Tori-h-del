import os

from dotenv import load_dotenv
from flask import Flask

from app.extensions import db


def create_app(test_config: dict | None = None) -> Flask:
    load_dotenv()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")

    if test_config is not None:
        app.config.update(test_config)
    else:
        mysql_host = os.getenv("MYSQL_HOST", "127.0.0.1")
        mysql_port = os.getenv("MYSQL_PORT", "3306")
        mysql_user = os.getenv("MYSQL_USER", "root")
        mysql_password = os.getenv("MYSQL_PASSWORD", "123456")
        mysql_db = os.getenv("MYSQL_DB", "flask_food_demo")

        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}?charset=utf8mb4"
        )

    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    db.init_app(app)

    from app.models import Dish
    from app.routes import bp

    app.register_blueprint(bp)

    @app.cli.command("init-db")
    def init_db_command() -> None:
        db.create_all()
        if Dish.query.count() == 0:
            db.session.add_all(
                [
                    Dish(name="宫保鸡丁", price=26.0, category="川菜"),
                    Dish(name="番茄鸡蛋面", price=16.0, category="面食"),
                ]
            )
            db.session.commit()
        print("数据库初始化完成")

    return app

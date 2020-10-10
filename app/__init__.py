import os
import click
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_restful import Api

from app.routes import frontend
from core.models import db, adduser, search_user_info
from core.settings import Setting as ST
from utils.my_logger import get_logger
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'xxx.sqlite')
# 请求结束后自动提交数据库修改
app.config['SQLALCHEMY_COMMMIT_ON_TEARDOWN'] = True
# 如果设置成 True (默认情况)，Flask-SQLAlchemy	将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
migrate = Migrate(app,db)
logger = get_logger()

def start_server():
    if ST.DEBUG:
        create_app().run(port=ST.SERVER_PORT, use_reloader=False, threaded=True)
    else:
        create_app().run(host='0.0.0.0', port=ST.SERVER_PORT, threaded=True)
        logger.info("start_server")


def create_app():
    app.config.from_object(__name__)
    # uri统一资源匹配符
    # SQLALCHEMY_DATABASE_URI配置数据库连接的参数

    Bootstrap(app)
    api = Api()
    api.init_app(app)
    db.init_app(app)
    ST.SERVERSTATICROOT = os.path.join(app.root_path, 'static')

    @app.cli.command("initdb")
    def initdb_command():
        db.drop_all()
        db.create_all()
        res = seeds()
        print(f"db create initialized")


    @app.cli.command("create-user")
    @click.argument("username",default="admin")
    @click.argument("password",default="admin")
    def create_user(username:str,password:str):
        adduser(username,password)

    @app.cli.command("search_user")
    @click.argument("user_id",default=1)
    def search(user_id):
        search_user_info(user_id)
    app.register_blueprint(frontend)
    return app

def seeds():
    print("db seeds")


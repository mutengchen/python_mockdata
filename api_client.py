import os
import random

from werkzeug.routing import Rule

from app import create_app, frontend
from flask import Flask

from core.settings import Setting as ST

@frontend.route("/<path>")
def test(path):
    #完全可以做到的
    #前端，一个添加api地址后缀，和对应需要返回的mock response
    #接受后保存在db里面，需要
    return path
#添加新的路由和地址
@frontend.route("/new_api")
def new_api():
    return "success"

@frontend.route("/delete_api")
def delete_api():
    return "failed"
@frontend.route("/api_list")
def api_list():
    return "api_list"
@frontend.route("/update_api")
def update_api():
    return "update_api"


if __name__ == '__main__':
    app = create_app()
    if ST.DEBUG:
        app.run(debug=True,port=ST.SERVER_PORT, host="127.0.0.1")
    else:
        app.run(port=ST.SERVER_PORT, host="0.0.0.0")


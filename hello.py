#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import request  
from flask import make_response, redirect, render_template
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime


app = Flask(__name__)  ## __name__ 比较多的用于__main__,程序主模块或者包名字, 直接启动当前.py脚本时，则__name__==__main__，否则等于__name__==模块名字
moment = Moment(app)
bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

@app.route('/ug')
def acquire_ug():
    user_agent=request.headers.get("User-Agent")  
    return "<p> Your browser is %s</p>" % user_agent

@app.route('/sc')
def setcookie():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie("answer", "42")
    return response

@app.route("/rc")
def gotobaidu():
    return redirect("http://www.baidu.com")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    manager.run()



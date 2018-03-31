#!/usr/bin/env python
# coding=utf-8
from flask import Flask


app = Flask(__name__)  ## __name__ 比较多的用于__main__,程序主模块或者包名字, 直接启动当前.py脚本时，则__name__==__main__，否则等于__name__==模块名字

@app.route('/')
def index():
    return '<h1>It\'s XiaoYu World!</h1>'


if __name__ == "__main__":
    app.run(debug=True)



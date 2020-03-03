
import openpyxl
import datetime
import os
import random
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import *
import config
import pymysql
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)
#建立与数据库中的表相一致的模型
class data(db.Model):
    __tablename__ = 'data'
    name=db.Column(db.String(255),nullable=True)
    Address=db.Column(db.String(255),nullable=True)
    Telephone=db.Column(db.String(255),nullable=True)
    Email=db.Column(db.String(255),nullable=True)
    Zip=db.Column(db.String(255),nullable=True)
    id=db.Column(db.Integer,nullable=True,primary_key=True)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
#对原始excle数据进行预处理
def Preprocessing():
    # 打开excel文件,获取工作簿对象
    wb = openpyxl.load_workbook('dangdang.xlsx')
    # 获取指定的表单
    ws = wb.active  # 当前活跃的表单
    for i in range(1, 101741):  # 获取i行第二列的值
        str=ws.cell(row=i, column=2).value
        str=str+""
        if str[0]=="住":
            print(i)
            print("  ")
        if str[0]=="(":
            print(i)
            print("  ")
    return 0

#查询的路由地址
@app.route('/query')
def query():
    return render_template("query.html")

#查询结果的路由地址
@app.route('/queryresult')
def queryresult():
    return render_template("queryresult.html")

@app.route('/')
def hello_world():

    return 'Hello World!'


if __name__ == '__main__':
    app.run()

#coding:utf8
from . import admin

@admin.route('/')
def admin():
    return "<h1>this is admin</h1>"
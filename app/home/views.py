#coding:utf8
from . import home

@home.route('/')
def home():
    return "<h1>this is home</h1>"
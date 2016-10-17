#!/usr/python3.5
#coding:utf-8

from flask import Flask

app = Flask(__name__)

@app.route("/")
def firstApp ():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run()

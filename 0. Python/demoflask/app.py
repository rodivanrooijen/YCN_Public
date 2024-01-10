from flask import Flask, render_template, request
from flask import Flask, render_template, request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/welkefiets")
def tweede():
    return "<p>Deze fiets</p>"


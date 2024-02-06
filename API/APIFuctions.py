from flask import Flask, request

app = Flask("hello")

@app.route("/")
def index():
    return "find cos, sin, tan of an angle"

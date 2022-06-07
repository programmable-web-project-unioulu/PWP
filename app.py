from flask import Flask
app = Flask("Hello")

#@app.route("/")
#def index():
#    return "you expected this to say hello, but it says \"donkey swings\" instead. Who would have guessed?"

""" Run "flask run" on virtualenv and correct folder to open service """

@app.route("/hello/<name>/")
def hello(name):
    return "Hello {}".format(name)

@app.route("/")
def index():
    return "How to use Flask. Info page"

@app.route("/add/<float:number_1>/<float:number_2>/")
def plus(number_1, number_2):
    return "{}".format(number_1 + number_2)

@app.route("/sub/<float:number_1>/<float:number_2>/")
def minus(number_1, number_2):
    return "{}".format(number_1 - number_2)

@app.route("/mul/<float:number_1>/<float:number_2>/")
def mult(number_1, number_2):
    return "{}".format(number_1 * number_2)

@app.route("/div/<float:number_1>/<float:number_2>/")
def div(number_1, number_2):
    """ Run http://localhost:5000/div/2.0/0.0/ on browser to see the results """
    if number_2 == 0.0:
        result = "NaN"
    else:
        result = number_1 / number_2
    return "{}".format(result)
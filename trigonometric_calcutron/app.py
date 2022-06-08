from flask import Flask, request
import math
import re
app = Flask("trigonometric_calcutron")


@app.route("/trig/<func>/")
def trig(func):
    try:
        if re.match("sin|cos|tan", func) is None:
            return "Operation not found", 404
        else:
            angle = request.args.get("angle")
            unit = request.args.get("unit")
        if unit == "degrees":
            angle = math.radians(float(angle))
        if func == "sin":
            angle = math.sin(float(angle))
        elif func == "cos":
            angle = math.cos(float(angle))
        elif func == "tan":
            angle = math.tan(float(angle))
    except KeyError:
        return "Invalid query parameter value(s)", 400
    except TypeError:
        return "Invalid query parameter value(s)", 400
    return "{}".format(angle)

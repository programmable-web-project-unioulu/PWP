from flask import Response, jsonify


def unauthorized() -> Response:
    output = {"error":
              {"msg": "401 error: Email or password is invalid."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 401
    return resp

def invalid_route() -> Response:
    output = {"error":
              {"msg": "404 error: This route is not supported"}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp
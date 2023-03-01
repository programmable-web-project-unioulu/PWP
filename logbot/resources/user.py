from flask import Response, request, abort, jsonify
from flask_restful import Resource
import json
from models.users import Users
from flask_jwt_extended import create_access_token, create_refresh_token
from errors import unauthorized, invalid_route
import datetime


class SignUp(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        
        """
        if not request.json:
            abort(415)
        try:
            data = request.get_json()
            new_user = Users(**data)
            new_user.save()
            user_id = {'id': str(new_user.id)}
        except KeyError:
            abort(400)
        
        return Response(json.dumps(user_id), 200)
            
class Login(Resource):
    """
    Flask-resftul resource for retrieving user web token.
    """
    @staticmethod
    def post() -> Response:
        """
        POST response method for retrieving user web token.
        :return: JSON object
        """
        if not request.json:
            abort(415)
        data = request.get_json()
        user = Users.objects.get(email=data.get('email'))
        auth_success = user.check_pw_hash(data.get('password'))
        if not auth_success:
            return unauthorized()
        else:
            expiry = datetime.timedelta(days=5)
            access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
            refresh_token = create_refresh_token(identity=str(user.id))
            return jsonify({'result': {'access_token': access_token,
                                       'refresh_token': refresh_token,
                                       'logged_in_as': f"{user.email}"}})
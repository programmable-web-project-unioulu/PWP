from flask_restful import Api

# Project Resources
from resources.authentication import SignUp, Login
from resources.user import UserApi


def create_routes(api: Api):
    """
    Adds resources to the api.
    :param api: Flask-RESTful Api Object
    
    """
    
    # User Authentication 
    api.add_resource(SignUp, '/authentication/signup/')
    api.add_resource(Login, '/authentication/login/')

    # Platform Users
    api.add_resource(UserApi, '/user/user_action')


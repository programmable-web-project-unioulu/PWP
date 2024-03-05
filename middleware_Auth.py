from flask import jsonify, request, g
from extensions import db
from models import ApiKey  # Import your ApiKey model here

def authenticate():
    if request.endpoint != 'static':
        api_key = request.headers.get('X-API-Key')
        if not api_key:
            return jsonify({'error': 'API key is missing'}), 401
        api_key_object = ApiKey.query.filter_by(key=api_key).first()
        if not api_key_object:
            return jsonify({'error': 'Invalid API key'}), 401
        g.current_api_key = api_key_object
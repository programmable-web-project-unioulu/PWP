import json
import pytest
import random
from .. import create_app 
from flask.testing import FlaskClient 
from data_models.models import Workout
from extensions import db
from werkzeug.datastructures import Headers

TEST_KEY = 'eaecf80e-3b2a-48b8-94c2-d754cf38'
RESOURCE_URL = '/api/workout'

@pytest.fixture
def client():
    config = {
        "SQLALCHEMY_DATABASE_URI": "mysql+mysqldb://admin:pwpdb7788@workoutplaylists.cpcoaea0i7dq.us-east-1.rds.amazonaws.com/test_workout_playlists",
        "TESTING": True
    }
        
    app = create_app(config)
    
    with app.app_context():
        db.create_all()
        _populate_db()
        
    app.test_client_class = AuthHeaderClient
    yield app.test_client()
    
class AuthHeaderClient(FlaskClient):

    def open(self, *args, **kwargs):
        api_key_headers = Headers({
            'X-API-Key': TEST_KEY
        })
        headers = kwargs.pop('headers', Headers())
        headers.extend(api_key_headers)
        kwargs['headers'] = headers
        return super().open(*args, **kwargs)

def _populate_db():
        
    for i in range(1, 4):
        intensity_list = ["slow","mild","intermediate","fast","extreme"]
        equipment_list = ["threadmill", "rwoing machine", "cardio equipment"]
        workout_type_list = ["running", "cardio", "Jumping"]
        w = Workout(
            workout_name="test-workout-{}".format(i),
            duration=random.random(),
            workout_intensity=random.choice(intensity_list),
            equipment=random.choice(equipment_list),
            workout_type=random.choice(workout_type_list)
        )
        db.session.add(w)
    db.session.commit()   

def test_get_workout(client):
    response = client.get("/api/workout/1")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert len(data) == 1

def test_get_workouts(client):
    response = client.get(RESOURCE_URL)
    assert response.status_code == 200

def test_post_workout(client):
        valid = _get_workout_json()
        invalidIntensityJson = _get_invalid_workout_json()

        # test with wrong content type
        resp = client.post(RESOURCE_URL, data="notjson")
        assert resp.status_code in (400, 415)

        #test with wrong intensity
        resp = client.post(RESOURCE_URL, json=invalidIntensityJson)
        assert resp.status_code == 400

        # test with valid and see that it exists afterward
        resp = client.post(RESOURCE_URL, json=valid)
        assert resp.status_code == 201
        
        # remove workout_name field for 400
        valid.pop("workout_name")
        resp = client.post(RESOURCE_URL, json=valid)
        assert resp.status_code == 400

def test_put_workout(client):
        valid = _get_workout_json()
        invalidJson = _get_invalid_workout_json()

        # test with wrong content type
        resp = client.put(f'{RESOURCE_URL}/1', data="notjson", headers=Headers({"Content-Type": "text"}))
        assert resp.status_code in (400, 415)

        #test with wrong id
        resp = client.put(f'{RESOURCE_URL}/id', json=valid)
        assert resp.status_code == 404
        
        # test with not avaliable id
        resp = client.put(f'{RESOURCE_URL}/10000', json=valid)
        assert resp.status_code == 404
        
        # test with valid
        resp = client.put(f'{RESOURCE_URL}/1', json=valid)
        assert resp.status_code == 204
        
        # remove field
        valid.pop("workout_name")
        resp = client.put(f'{RESOURCE_URL}/1', json=valid)
        assert resp.status_code == 204

        #invalid intensity
        resp = client.put(f'{RESOURCE_URL}/1', json=invalidJson)
        assert resp.status_code == 400

def test_delete_workout(client):
        resp = client.delete(f'{RESOURCE_URL}/105')
        assert resp.status_code == 204
        resp = client.delete(f'{RESOURCE_URL}/105')
        assert resp.status_code == 404
        resp = client.delete(f'{RESOURCE_URL}/id')
        assert resp.status_code == 404

def _get_workout_json():
    """
    Creates a valid workout JSON object to be used for PUT and POST tests.
    """
    
    return {
        "workout_name": "Sample Workout",
        "duration": 30.0,
        "workout_intensity": "slow",
        "equipment": "Dumbbells",
        "workout_type": "Strength"
    }

def _get_invalid_workout_json():
    """
    Creates an invalid workout JSON object to be used for PUT and POST tests.
    """
    
    return {
        "workout_name": "Sample Workout",
        "duration": 30.0,
        "workout_intensity": "invalid",
        "equipment": "Dumbbells",
        "workout_type": "Strength"
    }

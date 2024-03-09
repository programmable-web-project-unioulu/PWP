import json
import pytest
import random
from .. import create_app 
from flask.testing import FlaskClient 
from data_models.models import WorkoutPlan
from extensions import db
from werkzeug.datastructures import Headers

TEST_KEY = 'eaecf80e-3b2a-48b8-94c2-d754cf38'
RESOURCE_URL = '/api/workoutPlan'

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
        w = WorkoutPlan(
            plan_name="test-workout-plan-{}".format(i),
            duration=random.random(),
            user_id=24,
            playlist_id=1
        )
        db.session.add(w)
    db.session.commit()   

def test_get_workoutplan(client):
    response = client.get(f'{RESOURCE_URL}/10')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert len(data) == 1

# def test_get_workouts(client):
#     response = client.get(RESOURCE_URL)
#     assert response.status_code == 200

def test_post_workout(client):
        valid = _get_workout_plan_json()
        #invalidIntensityJson = _get_invalid_workout_json()

        # test with wrong content type
        resp = client.post(RESOURCE_URL, data="notjson")
        assert resp.status_code in (400, 415)

        #test with wrong intensity
        # resp = client.post(RESOURCE_URL, json=invalidIntensityJson)
        # assert resp.status_code == 400

        # test with valid and see that it exists afterward
        resp = client.post(RESOURCE_URL, json=valid)
        assert resp.status_code == 201
        
        # remove workout_name field for 400
        valid.pop("workout_name")
        resp = client.post(RESOURCE_URL, json=valid)
        assert resp.status_code == 400

def test_put_workout_plan(client):
        valid = _get_workout_plan_json()

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
        resp = client.put(f'{RESOURCE_URL}/10', json=valid)
        assert resp.status_code == 204
        
        # remove field
        valid.pop("plan_name")
        resp = client.put(f'{RESOURCE_URL}/10', json=valid)
        assert resp.status_code == 204

def test_delete_workout_plan(client):
        resp = client.delete(f'{RESOURCE_URL}/15')
        assert resp.status_code == 204
        resp = client.delete(f'{RESOURCE_URL}/15')
        assert resp.status_code == 404
        resp = client.delete(f'{RESOURCE_URL}/id')
        assert resp.status_code == 404

def _get_workout_plan_json():
    """
    Creates a valid workout plan JSON object to be used for PUT and POST tests.
    """
    
    return {
        "plan_name": "Sample Workout Plan",
        "duration": 30.0,
        "user_id": 24,
        "playlist_id": 1
    }


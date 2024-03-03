from flask import Blueprint
from flask_restful import Api
from resources.workout import WorkoutResource
from resources.workoutPlan import WorkoutPlanResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Add resources to the API
api.add_resource(WorkoutResource, "/workout/<workout_id>/")
api.add_resource(WorkoutPlanResource, "/workoutPlan/<workout_plan_id>/")

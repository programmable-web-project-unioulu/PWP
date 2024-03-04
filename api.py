from flask import Blueprint
from flask_restful import Api
from resources.workout import WorkoutResource
from resources.workoutPlan import WorkoutPlanResource
from resources.workout import WorkoutAddingResource
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(WorkoutResource, "/workout/<workout_id>/")
api.add_resource(WorkoutAddingResource, "/workout/")
api.add_resource(WorkoutPlanResource, "/workoutPlan/<workout_plan_id>/")

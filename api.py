from flask import Blueprint
from flask_restful import Api
from resources.workout import WorkoutResource
from resources.workoutPlan import WorkoutPlanResource
from resources.workout import WorkoutAddingResource
from resources.song import SongResource
from resources.song import SongListResource
from resources.playlist import PlaylistResource
from resources.playlist import CreatePlaylistResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(WorkoutResource, "/workout/<workout_id>/")
api.add_resource(WorkoutAddingResource, "/workout/")
api.add_resource(WorkoutPlanResource, "/workoutPlan/<workout_plan_id>/")
api.add_resource(SongResource, "/song/<song_id>/")
api.add_resource(SongListResource, "/song/")
api.add_resource(PlaylistResource, "/playlist/<playlist_id>/")
api.add_resource(CreatePlaylistResource, "/playlist/")

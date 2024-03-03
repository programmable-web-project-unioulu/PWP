from flask import jsonify, request
from flask_restful import Resource
from models import WorkoutPlan
from models import WorkoutPlanItem
from extensions import db

class WorkoutPlanResource(Resource):
    def get(self, workout_plan_id):
        workoutPlan = WorkoutPlan.query.get(workout_plan_id)
        workoutPlan_list = []
        if workoutPlan:
            workout_dict = {
                "workout_plan_id": workoutPlan.workout_plan_id,
                "plan_name": workoutPlan.plan_name,
                "duration": workoutPlan.duration,
                "user_id": workoutPlan.user_id,
                "playlist_id": workoutPlan.playlist_id
            }
            workoutPlan_list.append(workout_dict)
        return jsonify(workoutPlan_list)

    def post(self):
        data = request.json
        if not data or 'plan_name' not in data:
            return {"message": "No input data provided"}, 400
        
        if (data['duration'] is not None and not isinstance(data['duration'], float)):
            return {"message": "Duration must be a float"}, 400
        
        if (data['playlist_id'] is not None and not isinstance(data['playlist_id'], int)):
            return {"message": "Playlist Id must be an integer"}, 400

        plan_name = data['plan_name']
        existing_workout = WorkoutPlan.query.filter_by(plan_name=plan_name).first()
        if existing_workout:
            return {"error": "Workout plan name already exists"}, 409
        else:
            workoutPlan = WorkoutPlan(
                plan_name=data["plan_name"],
                duration=data["duration"],
                user_id=data["user_id"],
                playlist_id=data["playlist_id"]
            )
            db.session.add(workoutPlan)
            db.session.commit()
            
            saved_workout = WorkoutPlan.query.filter_by(plan_name=plan_name).first()
            if saved_workout:
                workoutPlanItem = WorkoutPlanItem(
                    plan_name=data["plan_name"],
                    duration=data["duration"],
                    user_id=data["user_id"],
                    playlist_id=data["playlist_id"]
                )
                db.session.add(workoutPlanItem)
                db.session.commit()
            else:
                return {"error": "No workout plan for the plan name"}, 404
        
        return "", 201

    def put(self, workout_plan_id):
        data = request.json
        if not data:
            return {"message": "No input data provided"}, 400

        workout = WorkoutPlan.query.get(workout_plan_id)
        if not workout:
            return {"message": "Workout plan not found"}, 404

        try:
            if 'plan_name' in data:
                workout.plan_name = data['plan_name']
            if 'duration' in data:
                workout.duration = data['duration']
            if 'user_id' in data:
                workout.user_id = data['user_id']
            if 'playlist_id' in data:
                workout.playlist_id = data['playlist_id']

            db.session.commit()
        except ValueError as e:
            return {"message": str(e)}, 400

        return "", 204

    def delete(self, workout_plan_id):
        workout = WorkoutPlan.query.get(workout_plan_id)
        if not workout:
            return {"message": "Workout plan not found"}, 404

        db.session.delete(workout)
        db.session.commit()

        return "", 204
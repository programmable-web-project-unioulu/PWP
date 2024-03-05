from flask import jsonify, request
from flask_restful import Resource
from models import Workout
from extensions import db

class WorkoutResource(Resource):
    def get(self, workout_id):
        workout = Workout.query.get(workout_id)
        workout_list = []
        if workout:
            workout_dict = {
                "workout_id": workout.workout_id,
                "workout_name": workout.workout_name,
                "duration": workout.duration,
                "workout_intensity": workout.workout_intensity,
                "equipment": workout.equipment,
                "workout_type": workout.workout_type
            }
            workout_list.append(workout_dict)
        return jsonify(workout_list)

    def put(self, workout_id):
        data = request.json
        if not data:
            return {"message": "No input data provided"}, 400

        workout = Workout.query.get(workout_id)
        if not workout:
            return {"message": "Workout not found"}, 404

        try:
            if 'workout_name' in data:
                workout.workout_name = data['workout_name']
            if 'duration' in data:
                workout.duration = data['duration']
            if 'workout_intensity' in data:
                workout.workout_intensity = data['workout_intensity']
            if 'equipment' in data:
                workout.equipment = data['equipment']
            if 'workout_type' in data:
                workout.workout_type = data['workout_type']

            db.session.commit()
        except ValueError as e:
            return {"message": str(e)}, 400

        return "", 204

    def delete(self, workout_id):
        workout = Workout.query.get(workout_id)
        if not workout:
            return {"message": "Workout not found"}, 404

        db.session.delete(workout)
        db.session.commit()

        return "", 204
    
class WorkoutAddingResource(Resource):
        def post(self):
            data = request.json
            if not data or 'workout_name' not in data:
                return {"message": "No input data provided"}, 400
            
            if (data['duration'] is not None and not isinstance(data['duration'], float)):
                return {"message": "Duration must be a float"}, 400

            workout_name = data['workout_name']
            existing_workout = Workout.query.filter_by(workout_name=workout_name).first()
            if existing_workout:
                return {"error": "workout_name already exists"}, 409
            try:
                workout = Workout(
                    workout_name=data["workout_name"],
                    duration=data["duration"],
                    workout_intensity=data["workout_intensity"],
                    equipment=data["equipment"],
                    workout_type=data["workout_type"]
                )
                db.session.add(workout)
                db.session.commit()
            except ValueError as e:
                return {"message": str(e)}, 400
            return "", 201
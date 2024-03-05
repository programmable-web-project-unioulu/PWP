from flask import jsonify, request
from flask_restful import Resource
from models import Playlist
from models import PlaylistItem
from models import Workout
from models import Song
from extensions import db

# endpoints

# get a playlist with all songs


class PlaylistResource(Resource):
    def get(self, playlist_id):
        playlist = Playlist.query.get(playlist_id)
        playlist_items = PlaylistItem.query.filter_by(playlist_id=playlist_id).all()
               
        songs_list = []
        for item in playlist_items:
            song = Song.query.get(item.song_id)
            if song:
                song_dict = {
                    "song_id": song.song_id,
                    "song_name": song.song_name,
                    "artist": song.song_artist,
                    "genre": song.song_genre,
                    "duration": song.song_duration
                }
            songs_list.append(song_dict)

        playlist_dict = {}

        if playlist:
            playlist_dict = {
            "playlist_id": playlist.playlist_id,
            "playlist_duration": playlist.playlist_duration,
            "songs_list": songs_list
            }
        return jsonify(playlist_dict)
    
    def delete(self, playlist_id):
        playlist = Playlist.query.get(playlist_id)
        if not playlist:
            return {"message": "Playlist not found"}, 404

        playlist_items = PlaylistItem.query.filter_by(playlist_id=playlist_id).all()

        # Delete playlist items
        for item in playlist_items:
            db.session.delete(item)

        # Delete playlist
        db.session.delete(playlist)
        db.session.commit()

        return "", 204


class CreatePlaylistResource(Resource):
    def post(self):
        data = request.json
        if not data or 'workout_ids' not in data:
            return {"message": "Invalid input data on CreatePlayList"}, 400

        # playlist_name = data['playlist_name']
        workout_ids = data['workout_ids']

        print(workout_ids)

        songs_list = []
        total_workouts_duration = 0.0

        # Add songs to playlist for each workout
        for workout_id in workout_ids:
            workout = Workout.query.get(workout_id)
            if workout:
                duration = workout.duration
                intensity = workout.workout_intensity
                genre = ""

                # Determine genre based on intensity
                if intensity == "slow":
                    genre = ["Ambient", "Classical", "Jazz"]
                elif intensity == "mild":
                    genre = ["Pop", "R&B", "Indie"]
                elif intensity == "intermediate":
                    genre = ["Rock", "Hip-hop", "EDM"]
                elif intensity == "fast":
                    genre = ["Techno", "Dance", "House"]
                elif intensity == "extreme":
                    genre = ["Metal", "Hardcore", "Dubstep"]

                # Get songs based on workout duration and genre
                
                songs = Song.query.filter(Song.song_genre.in_(genre)).all()
                temp_duration = 0.0
                for song in songs:
                    song_dict = {
                        "song_id": song.song_id
                    }
                    songs_list.append(song_dict)
                    temp_duration += song.song_duration
                    if temp_duration >= duration:
                        break
                
                total_workouts_duration = total_workouts_duration + temp_duration

        # Create playlist
        playlist = Playlist(playlist_duration=total_workouts_duration)
        db.session.add(playlist)
        db.session.commit()

        # Add songs related to playlist to playlist_item table
        for song in songs_list:
            playlist_item = PlaylistItem(
                playlist_id=playlist.playlist_id,
                song_id=song['song_id'],
            )
            db.session.add(playlist_item)
        db.session.commit()

        return {"message": "Playlist created successfully", "playlist_id": playlist.playlist_id}, 201
    
    # user can change the playlist song order

    # def put(self, workout_plan_id):
    #     data = request.json
    #     if not data:
    #         return {"message": "No input data provided"}, 400

    #     workout = WorkoutPlan.query.get(workout_plan_id)
    #     if not workout:
    #         return {"message": "Workout plan not found"}, 404

    #     try:
    #         if 'plan_name' in data:
    #             workout.plan_name = data['plan_name']
    #         if 'duration' in data:
    #             workout.duration = data['duration']
    #         if 'user_id' in data:
    #             workout.user_id = data['user_id']
    #         if 'playlist_id' in data:
    #             workout.playlist_id = data['playlist_id']

    #         db.session.commit()
    #     except ValueError as e:
    #         return {"message": str(e)}, 400

    #     return "", 204

    # def delete(self, workout_plan_id):
    #     workout = WorkoutPlan.query.get(workout_plan_id)
    #     if not workout:
    #         return {"message": "Workout plan not found"}, 404

    #     db.session.delete(workout)
    #     db.session.commit()

    #     return "", 204
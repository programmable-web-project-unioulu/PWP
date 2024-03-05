from prisma.models import Poll
from api.models.poll_dtos import PollDto
from flask import make_response, request, Blueprint, Response, jsonify
from flask_restful import Api, Resource
from prisma.errors import UniqueViolationError
from werkzeug.exceptions import BadRequest, NotFound

poll = Blueprint("poll", __name__, url_prefix="/polls")
poll_api = Api(poll)


class Poll_Id(Resource):
    def get(self, poll_id):
        return Response(status=501)


class PollItems(Resource):
    def get(self, poll_id):
        try:
            poll = Poll.prisma().find_first(
                where={"id": poll_id}, include={"items": True}
            )
        except UniqueViolationError:
            raise BadRequest

        response_data = []
        for poll_item in poll.items:
            response_data.append(
                {"description": poll_item.description, "votes": poll_item.votes}
            )
        if poll.items is not None:
            response = {"pollItems": response_data}, 200
        else:
            response = "No poll items found!", 404
        return make_response(response)


class PollCreate(Resource):
    def post(self):
        poll_dto = PollDto.from_json(request.json)
        try:
            created_poll = Poll.prisma().create(data=poll_dto.to_insertable())
            # finding the created poll
            poll = Poll.prisma().find_first(where={"title": poll_dto.title})
        except UniqueViolationError:
            raise BadRequest("username not unique")
        return make_response({"poll_id": poll.id})


class PollUpdate(Resource):
    def put(self, poll_id):
        updated_data = request.json
        try:
            # Attempt to update the poll with the given ID
            Poll.prisma().update(where={"id": poll_id}, data=updated_data)
            # Prepare a success response message
            response_data = {"message": "Poll updated successfully"}
        except Exception as e:
            # Handle exceptions, such as BadRequest for validation errors
            return make_response(
                jsonify({"message": str(e)}), 400
            )  # Use appropriate status code

        # Return a successful response with serialized data
        return make_response(jsonify(response_data), 200)


class PollDelete(Resource):
    def delete(self, poll_id):
        poll = Poll.prisma().find_first(where={"id": poll_id})
        if poll is None:
            raise NotFound(f"Poll with ID {poll_id} not found")

        Poll.prisma().delete(where={"id": poll_id})
        return jsonify({"message": "Poll deleted successfully"})


class PollGetAll(Resource):
    def get(self):
        try:
            # Assuming Poll.prisma().find_many() returns a list of Poll objects
            all_polls = Poll.prisma().find_many()

            # Convert all_polls to a list of dictionaries for JSON serialization
            polls_data = [poll.dict() for poll in all_polls]
        except Exception as e:
            # Handle any exceptions that arise
            raise BadRequest(str(e))

        # Use jsonify to serialize and return the response
        return jsonify(polls_data)


class PollGetSingle(Resource):
    def get(self, poll_id):
        try:
            # Attempt to find the poll by its ID
            poll = Poll.prisma().find_first(where={"id": poll_id})
            if not poll:
                # Poll not found, return a 404 response
                return make_response(jsonify({"message": "Poll not found"}), 404)

            # Serialize the poll object to a dictionary before passing to jsonify
            poll_data = {
                "id": poll.id,
                "userId": poll.userId,
                "title": poll.title,
                "description": poll.description,
                "expires": poll.expires,
                "private": poll.private,
                "multipleAnswers": poll.multipleAnswers,
            }
        except Exception as e:
            # Handle general exceptions
            return make_response(jsonify({"message": str(e)}), 500)

        # Return the serialized poll data as JSON
        return jsonify(poll_data)


poll_api.add_resource(PollItems, "/<poll_id:poll_id>/pollitems")
poll_api.add_resource(PollCreate, "")
poll_api.add_resource(PollUpdate, "/<poll_id:poll_id>/update")
poll_api.add_resource(PollDelete, "/<poll_id:poll_id>/delete")
poll_api.add_resource(PollGetAll, "/all")
poll_api.add_resource(PollGetSingle, "/<poll_id:poll_id>")

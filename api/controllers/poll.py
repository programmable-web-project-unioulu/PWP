from prisma.models import Poll
from api.models.poll_dtos import PollDto
from flask import make_response, request, Blueprint, Response
from flask_restful import Api, Resource
from prisma.errors import UniqueViolationError
from werkzeug.exceptions import BadRequest

poll = Blueprint("poll", __name__, url_prefix="/polls")
poll_api = Api(poll)


class Poll_Id(Resource):
    def get(self, poll_id):
        return Response(status=501)


class PollItems(Resource):
    """
    Gets all PollItems within a specified Poll.

    Send a GET request to /polls/<poll_id:poll_id>/pollitems with:
    "poll_id": Poll ID to query.

    returns:

    {
    
    "pollItems": list of PollItems.

    }
    """
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
    """
    Creates a Poll.

    Send a POST request to /polls with:
    {
    
    "userId": id of the user who wants to create the Poll.
    "title": title of the Poll.
    "description": description of the Poll.
    "expires": expiry date of Poll.
    "multipleAnswers": whether multiple answers should be allowed or not.
    "private": whether the Poll is private or not.

    }

    returns:

    {
    
    "poll_id": ID of the created Poll.

    }
    """
    def post(self):
        poll_dto = PollDto.from_json(request.json)
        try:
            Poll.prisma().create(data=poll_dto.to_insertable())
            # finding the created poll
            poll = Poll.prisma().find_first(where={"title": poll_dto.title})
        except UniqueViolationError:
            raise BadRequest("username not unique")
        return make_response({"poll_id": poll.id})


poll_api.add_resource(PollItems, "/<poll_id:poll_id>/pollitems")
poll_api.add_resource(PollCreate, "")

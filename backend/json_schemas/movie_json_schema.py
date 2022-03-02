
def get_movie_json_schema():
    schema = {
        "type": "object",
        "required": ["title", "director", "length", "release_date", "category_id"]
    }

    props = schema["properties"] = {}
    props["title"] = {
        "description": "Movie's title",
        "type": "string"
    }
    props["director"] = {
        "description": "The name of the director of the movie",
        "type": "string"
    }
    props["length"] = {
        "description": "The length of the movie in seconds",
        "type": "integer"
    }
    props["release_date"] = {
        "description": "The release date of the movie",
        "type": "string",
        "format": "date-time"
    }
    props["category_id"] = {
        "description": "The id of the movie's category which acts as foreign key",
        "type": "integer"
    }
    return schema

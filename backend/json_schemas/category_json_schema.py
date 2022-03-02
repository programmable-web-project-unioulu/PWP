
def get_user_json_schema():
        schema = {
            "type": "object",
            "required": ["id", "title"]
        }

        props = schema["properties"] = {}
        props["id"] = {
            "description": "Category's id",
            "type": "integer"
        }
        props["title"] = {
            "description": "The name of the category",
            "type": "string"
        }
        return schema

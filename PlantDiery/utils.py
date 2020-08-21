import json
from flask import Response, request, url_for
from PlantDiery.constants import *
from PlantDiery.models import *

def create_error_response(status_code, title, message=None):

    resource_url = request.path
    body = MasonBuilder(resource_url=resource_url)
    body.add_error(title, message)
    body.add_control("profile", href=ERROR_PROFILE)
    return Response(json.dumps(body), status_code, mimetype=MASON)

class MasonBuilder(dict):
    """
    A convenience class for managing dictionaries that represent Mason
    objects. It provides nice shorthands for inserting some of the more
    elements into the object but mostly is just a parent for the much more
    useful subclass defined next. This class is generic in the sense that it
    does not contain any application specific implementation details.
    """

    def add_error(self, title, details):
        """
        Adds an error element to the object. Should only be used for the root
        object, and only in error scenarios.
        Note: Mason allows more than one string in the @messages property (it's
        in fact an array). However we are being lazy and supporting just one
        message.
        : param str title: Short title for the error
        : param str details: Longer human-readable description
        """

        self["@error"] = {
                "@message": title,
                "@messages": [details],
                }

    def add_namespace(self, ns, uri):
        """
        Adds a namespace element to the object. A namespace defines where our
        link relations are coming from. The URI can be an address where
        developers can find information about our link relations.
        : param str ns: the namespace prefix
        : param str uri: the identifier URI of the namespace
        """

        if "@namespaces" not in self:
            self["@namespaces"] = {}

        self["@namespaces"][ns] = {
                "name": uri
                }

    def add_control(self, ctrl_name, href, **kwargs):
        """
        Adds a control property to an object. Also adds the @controls property
        if it doesn't exist on the object yet. Technically only certain
        properties are allowed for kwargs but again we're being lazy and don't
        perform any checking.
        The allowed properties can be found from here
        https://github.com/JornWildt/Mason/blob/master/Documentation/Mason-draft-2.md
        : param str ctrl_name: name of the control (including namespace if any)
        : param str href: target URI for the control
        """

        if "@controls" not in self:
            self["@controls"] = {}

        self["@controls"][ctrl_name] = kwargs
        self["@controls"][ctrl_name]["href"] = href


class PlantBuilder(MasonBuilder):

# POST
    # GENERAL PLANT
    def add_control_add_general_plant(self):
        self.add_control(
            "plandi:add-generalplant",
            url_for("api.plantgeneralcollection"),
            method="POST",
            encoding="json",
            title="Add new general plant information",
            schema=PlantGeneral.get_schema()
        )
    ## PLANT
    def add_control_add_plant(self):
        self.add_control(
            "plandi:add-plant",
            url_for("api.plantcollection"),
            method="POST",
            encoding="json",
            title="Add new plant information",
            schema=Plant.get_schema()
        )
    ## DIARY
    def add_control_add_diary_entry(self):
        self.add_control(
            "plandi:add-entry",
            url_for("api.diarycollection"),
            method="POST",
            encoding="json",
            title="Add new diary entry",
            schema=Diary.get_schema()
        )

## DELETE
    # GENERAL PLANT
    def add_control_delete_general_plant(self, plant_id):
        self.add_control(
            "plandi:delete",
            url_for("api.generalplant", plant_id=plant_id),
            method="DELETE",
            title="Delete given general plant information"
        )
    # PLANT
    def add_control_delete_plant(self, name):
        self.add_control(
            "plandi:delete",
            url_for("api.plantitem", name=name),
            method="DELETE",
            title="Delete given plant information"
        )
    # DIARY
    def add_control_delete_diary_entry(self, entry_id):
        self.add_control(
            "plandi:delete",
            url_for("api.plantitem", entry_id=entry_id),
            method="DELETE",
            title="Delete given diary entry"
        )
## GET
    # GENERAL PLANT
    def add_control_all_general_plants(self):
        self.add_control(
            "plandi:plantsgeneral-all",
            url_for("api.plantgeneralcollection"),
            method="GET",
            encoding="json"
        )
    # PLANT
    def add_control_all_plants(self):
        self.add_control(
            "plandi:plants-all",
            url_for("api.plantcollection"),
            method="GET",
            encoding="json"
        )
    # DIARY
    def add_control_all_diary(self):
        self.add_control(
            "plandi:diaryentry-all",
            url_for("api.diarycollection"),
            method="GET",
            encoding="json"
        )
# PUT
    # GENERAL PLANT
    def add_control_modify_general_plant(self, plant_id):
        self.add_control(
            "edit",
            url_for("api.plantgeneral", plant_id=plant),
            method="PUT",
            encoding="json",
            title="Edit given general plant information",
            schema=PlantGeneral.get_schema()
        )
    # PLANT
    def add_control_modify_plant(self, name):
        self.add_control(
            "edit",
            url_for("api.plantitem", name=name),
            method="PUT",
            encoding="json",
            title="Edit given plant information",
            schema=PlantGeneral.get_schema()
        )

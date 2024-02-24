from dataclasses import asdict
from typing import List
from werkzeug.exceptions import BadRequest


class BaseDto:
    """All other DTOs inherit stuff from this one."""

    def to_insertable(self) -> dict:
        """Convert the DTO into a dict for use with Prisma"""
        return {k: str(v) for k, v in asdict(self).items()}

    @staticmethod
    def validate(props: List[tuple], data: dict):
        """Validate the data properties
        data: request.json
        props: ex: [('username', str)]

        raises BadRequest error if invalid
        """
        errors = []
        for prop in props:
            k, t = prop
            val = data.get(k)
            if val is None:
                errors.append(f"Missing property '{k}'")
            elif not isinstance(val, t):
                errors.append(f"Property '{k}' not of type str")
        if len(errors) > 0:
            raise BadRequest(errors)

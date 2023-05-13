""" Validator for the data
"""


# It is necessary to ignore mypy Cerberus errors because it apparently misses
# library stubs or py.typed marker
from cerberus import Validator  # type: ignore

schema = {
            "name": {
                "type": "string",
                "minlength": 3,
                "maxlength": 80,
                "required": True,
                "empty": False
            }
}


validator = Validator(schema)
data = {"name": "Jo"}
if not validator.validate(data):
    print('Invalid Data:')
    print(validator.errors)

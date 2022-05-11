from marshmallow import ValidationError
from utils.exceptions import BadRequestException

class Formatter:
    def __init__(self, schema):
        self.schema = schema()

    
    def fields(self, payload, partial_fields=False):
        try:
            return self.schema.load(payload, partial=partial_fields)
        except ValidationError as e:
            raise BadRequestException(e.messages)

    def obj_db_to_dict(self, obj_db):
        return {field.name: getattr(obj_db, field.name) for field in obj_db.__table__.columns}

    def response(self, payload_list): 
        return list(map(lambda payload: self.fields(self.obj_db_to_dict(payload)), payload_list))

    def value_exist_in_db(self, db, query, error='Not exist'):
        if not db(**query):
            raise BadRequestException(error)
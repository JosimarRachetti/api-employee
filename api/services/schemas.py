from datetime import datetime
import json
from utils.decimal import DecimalEncoder
from marshmallow import Schema, fields, validate, EXCLUDE, post_load, pre_load


class EmployeeSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    registration = fields.Int()
    name = fields.Str(required=True, error_messages={"required": "name is required."})
    last_name = fields.Str(required=True)
    code_position = fields.Int(required=True, error_messages={"required": "code position is required."})
    salary = fields.Decimal(required=True, error_messages={"required": "salary is required."})
    password = fields.Str(required=True, error_messages={"required": "password is required."})
    status = fields.Str(required=True, validate=validate.OneOf(["ATIVO", "DESATIVADO"]), error_messages={"required": "status is required."})
    create = fields.Str(missing=str(datetime.now().isoformat()))
    last_update = fields.Str(missing=str(datetime.now().isoformat()))

    @post_load
    def to_json(self,  data, **kwargs):
        return json.loads(json.dumps(data, cls=DecimalEncoder))

class LeaderSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Int()
    code_employee = fields.Int(required=True, error_messages={"required": "code employee is required."})
    code_position = fields.Int(required=True, error_messages={"required": "code position is required."})
    code_team = fields.Str(required=True, error_messages={"required": "code team is required."})
    create = fields.Str(missing=str(datetime.now().isoformat()))

class PositionSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Int()
    title = fields.Str(required=True, error_messages={"required": "title is required."})
    description = fields.Str(required=True, error_messages={"required": "description is required."})
    code_team = fields.Str(required=True, error_messages={"required": "code team is required."})
    status = fields.Str(required=True, validate=validate.OneOf(["OCUPADA", "ABERTA"]), error_messages={"required": "status is required."})
    create = fields.Str(missing=str(datetime.now().isoformat()))
    last_update = fields.Str(missing=str(datetime.now().isoformat()))
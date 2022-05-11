from flask import Flask
from flask_restful import Api
from services.schemas import LeaderSchema, EmployeeSchema, PositionSchema

from controller.leader import Leader
from model.leader import LeaderDB

from controller.employee import Employee
from model.employee import EmployeeDB

from controller.position import Position
from model.position import PositionDB

from database.database import Connection

app = Flask(__name__)
api = Api(app)

api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': Connection, 'position_model': PositionDB, 'employee_model': EmployeeDB, 'employee_schema': EmployeeSchema})
api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': Connection, 'leader_model': LeaderDB, 'position_model': PositionDB, 'employee_model': EmployeeDB, 'leader_schema': LeaderSchema})
api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': Connection, 'position_model': PositionDB, 'position_schema': PositionSchema})

if __name__ == '__main__':
    app.run(debug=True)

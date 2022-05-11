from flask_restful import Resource, request
from services.formatter import Formatter
from utils.exceptions import BadRequestException


class Leader(Resource):
    def __init__(self, db, leader_model, position_model, employee_model, leader_schema):
        self.connection_db = db()
        self.db = self.connection_db.create_session()
        self.leader_db = leader_model(self.db)
        self.position_db = position_model(self.db)
        self.employee_db = employee_model(self.db)
        self.formatter = Formatter(leader_schema)

    def post(self, **kwargs):
        try:
            data = self.formatter.fields(request.json)
            
            self.formatter.value_exist_in_db(self.position_db.find_position, {"id": data["code_position"], "status": "ABERTA"}, 'is necessary a valida code position.')
            if not self.employee_db.update_employee(**{'registration': data["code_employee"], "code_position": data["code_position"]}):
                raise BadRequestException('is necessary a valida code employee.')

            leader = self.leader_db.new_leader(**data)
            self.db.commit()
            return {"message": self.formatter.response([leader])}, 201
        except BadRequestException as e:
            self.db.rollback()
            return {"message": e.args[0]}, 400
        except Exception as e:
            self.db.rollback()
            return {"message": "internal error"}, 500
        finally:
            self.db.close()

    def get(self, **kwargs):
        try:
            query_parameters = self.formatter.fields(payload=request.args, partial_fields=True)
            leader_list = self.leader_db.find_leader(**query_parameters)
            
            if not leader_list:
                self.db.rollback()
                return {"message": "leader not found"}, 404

            self.db.commit()
            return {"message": self.formatter.response(leader_list)}, 200
        except BadRequestException as e:
            self.db.rollback()
            return {"message": e.args[0]}, 400
        except Exception as e:
            self.db.rollback()
            return {"message": "internal error"}, 500
        finally:
            self.db.close()

    def put(self, **kwargs):
        try:
            if not kwargs.get('id'):
                raise BadRequestException('is necessary a id leader to update.')

            data = {**request.json, **{"id":kwargs.get('id')}}
            data = self.formatter.fields(data, partial_fields=True)

            if 'code_position' in data:
                self.formatter.value_exist_in_db(self.position_db.find_position, {"id": data["code_position"], "status": "ABERTA"}, 'is necessary a valide code position.')

            if 'code_employee' in data:
                self.formatter.value_exist_in_db(self.employee_db.find_employee, {"registration": data["code_employee"]}, 'is necessary a valide code employee.')
            

            leader = self.leader_db.update_leader(**data)

            if not leader:
                self.db.rollback()
                return {"message": "leader not found"}, 404

            if not self.employee_db.update_employee(**{'registration': leader.code_employee, "code_position": leader.code_position}):
                raise BadRequestException("is not possible update employee")
             
            self.db.commit()
            return {"message": self.formatter.response([leader])}, 200
        except BadRequestException as e:
            self.db.rollback()
            return {"message": e.args[0]}, 400
        except Exception as e:
            self.db.rollback()
            return {"message": "internal error"}, 500
        finally:
            self.db.close()




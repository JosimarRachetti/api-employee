
from flask_restful import Resource, request
from services.formatter import Formatter
from utils.exceptions import BadRequestException




class Employee(Resource):
    def __init__(self, db, position_model, employee_model, employee_schema):
        self.connection_db = db()
        self.db = self.connection_db.create_session()
        self.position_db = position_model(self.db)
        self.employee_db = employee_model(self.db)
        self.formatter = Formatter(employee_schema)

    def post(self, **kwargs):
        try:
            payload = request.json
            data = self.formatter.fields(payload)
            self.formatter.value_exist_in_db(self.position_db.find_position, {"id": data["code_position"], "status": "ABERTA"}, "is necessary a code position valid.")
            employee = self.employee_db.new_employee(**data)
            self.db.commit()
            return {"message": self.formatter.response([employee])}, 201
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
            employee_list = self.employee_db.find_employee(**query_parameters)
            
            if not employee_list:
                self.db.rollback()
                return {"message": "employee not found"}, 404

            self.db.commit()
            return {"message": self.formatter.response(employee_list)}, 200
        except Exception as e:
            self.db.rollback()
            return {"message": "internal error"}, 500
        finally:
            self.db.close()

    def put(self, **kwargs):
        try:
            if not kwargs.get('registration'):
                raise BadRequestException('is necessary registration to update')
                
            data = {**request.json, **{"registration": kwargs.get('registration')}}
            data = self.formatter.fields(data, partial_fields=True)

            if 'code_position' in data:
                self.formatter.value_exist_in_db(self.position_db.find_position, {'id': data['code_position'] , "status": "ABERTA"}, "is necessary a code position valid.")
            
            employee = self.employee_db.update_employee(**data)
            if not employee:
                return {"message": "employee not found"}, 404
            
            self.db.commit()
            return {"message": self.formatter.response([employee])}, 200
        except BadRequestException as e:
            self.db.rollback()
            return {"message": e.args[0]}, 400
        except Exception as e:
            self.db.rollback()
            return {"message": "internal error"}, 500
        finally:
            self.db.close()

    def delete(self, **kwargs):
        try:
            if not kwargs.get('registration'):
                raise BadRequestException('is necessary a valid registration to delete')
                
            data = {"registration": kwargs.get('registration')}
            data = self.formatter.fields(data, partial_fields=True)
            self.employee_db.delete_employee(**data)

            self.db.commit()
            return {"message": "delete sucessful"}, 200
        except BadRequestException as e:
            self.db.rollback()
            return {"message": e.args[0]}, 400
        except Exception as e:
            self.db.rollback()
            return {"message": "internal error"}, 500
        finally:
            self.db.close()



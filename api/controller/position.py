from flask_restful import Resource, request
from services.formatter import Formatter
from utils.exceptions import BadRequestException




class Position(Resource):
    def __init__(self, db, position_model, position_schema):
        self.connection_db = db()
        self.db = self.connection_db.create_session()
        self.position_db = position_model(self.db)
        self.formatter = Formatter(position_schema)

    def post(self, **kwargs):
        try:
            payload = request.json
            data = self.formatter.fields(payload)
            position = self.position_db.new_position(**data)
            self.db.commit()
            return {"message": self.formatter.response([position])}, 201
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
            position_list = self.position_db.find_position(**query_parameters)
            
            if not position_list:
                self.db.rollback()
                return {"message": "position not found"}, 404

            self.db.commit()
            return {"message": self.formatter.response(position_list)}, 200
        except Exception as e:
            self.db.rollback()
            return {"message": "internal error"}, 500
        finally:
            self.db.close()

    def put(self, **kwargs):
        try:
            if not kwargs.get('id'):
                raise BadRequestException('is necessary id to update')
            
            data = {**request.json, **{"id":kwargs.get('id')}}
            data = self.formatter.fields(data, partial_fields=True)
            position = self.position_db.update_position(**data)
            if not position:
                return {"message": "position not found"}, 404

            self.db.commit()
            return {"message": self.formatter.response([position])}, 200
        except BadRequestException as e:
            self.db.rollback()
            return {"message": e.args[0]}, 400
        except Exception as e:
            self.db.rollback()
            return {"message": "internal error"}, 500
        finally:
            self.db.close()
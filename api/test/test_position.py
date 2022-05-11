from flask import Flask
from flask_restful import Api

import unittest
from controller.position import Position

from services.schemas import PositionSchema

from test.mocks import MockPositionDB, MockConnection, mock_position


class PositionControllerTestCase(unittest.TestCase):
  
    def test_post_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"post": 200}
        MockPositionDB.value_return = mock_position()

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": "ABERTA"
                  }
        resp = app.post('/position', json=payload)
        self.assertEqual(resp._status_code, 201)

    def test_post_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"post": 200}
        MockPositionDB.value_return = mock_position()

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": ""
                  }
        resp = app.post('/position', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_post_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"post": 500}
        MockPositionDB.value_return = mock_position()

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": "ABERTA"
                  }
        resp = app.post('/position', json=payload)
        self.assertEqual(resp._status_code, 500)

    def test_put_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"put": 200}
        MockPositionDB.value_return = mock_position()

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": "ABERTA"
                  }
        resp = app.post('/position/100', json=payload)
        self.assertEqual(resp._status_code, 201)

    def test_put_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"put": 200}
        MockPositionDB.value_return = mock_position()

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": ""
                  }
        resp = app.post('/position', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_put_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"put": 404}

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": ""
                  }
        resp = app.post('/position/100', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_put_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"post": 500}
        MockPositionDB.value_return = mock_position()

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": "ABERTA"
                  }
        resp = app.post('/position/100', json=payload)
        self.assertEqual(resp._status_code, 500)

    def test_get_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = mock_position()

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": "ABERTA"
                  }
        resp = app.post('/position/100', json=payload)
        self.assertEqual(resp._status_code, 201)

    def test_get_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"get": 404}

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": ""
                  }
        resp = app.post('/position/100', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_get_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockPositionDB.methods_return = {"post": 500}
        MockPositionDB.value_return = mock_position()

        api.add_resource(Position, '/position', '/position/<id>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB,  'position_schema': PositionSchema})

        app = app.test_client()
        payload = {
                    "title":"Analista desenvolvimento",
                    "description": "testar e construir apis",
                    "code_team": "AA22",
                    "status": "ABERTA"
                  }
        resp = app.post('/position/100', json=payload)
        self.assertEqual(resp._status_code, 500)

if __name__ == "__main__":
    unittest.main()

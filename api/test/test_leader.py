from flask import Flask
from flask_restful import Api

import unittest
from controller.leader import Leader

from services.schemas import LeaderSchema

from test.mocks import MockPositionDB, MockEmployeeDB, MockLeaderDB, MockConnection, mock_position, mock_leader, mock_employee


class PositionControllerTestCase(unittest.TestCase):
  
    def test_post_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = mock_position()

        MockLeaderDB.methods_return = {"post": 200}
        MockLeaderDB.value_return = mock_leader()


        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.post('/leader', json=payload)
        self.assertEqual(resp._status_code, 201)

    def test_post_response_bad_request_employee_not_found(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 404}

        MockPositionDB.methods_return = {"get":200}
        MockPositionDB.value_return = mock_position()

        MockLeaderDB.methods_return = {"post":200}
        MockLeaderDB.value_return = mock_leader()


        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.post('/leader', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_post_response_bad_request_code_not_valid(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()
        
        MockPositionDB.methods_return = {"get": 404}

        MockLeaderDB.methods_return = {"post": 200}
        MockLeaderDB.value_return = mock_leader()

        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.post('/leader', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_post_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = mock_position()

        MockLeaderDB.methods_return = {"post": 500}

        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.post('/leader', json=payload)
        self.assertEqual(resp._status_code, 500)

    def test_put_response_sucessful(self):
          app = Flask(__name__)
          api = Api(app)

          MockEmployeeDB.methods_return = {"put": 200}
          MockEmployeeDB.value_return = mock_employee()

          MockPositionDB.methods_return = {"get": 200}
          MockPositionDB.value_return = mock_position()
          
          MockLeaderDB.methods_return = {"put": 200}
          MockLeaderDB.value_return = mock_leader()


          api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

          app = app.test_client()
          payload = {
                      "code_employee": 1001,
                      "code_position": 100,
                      "code_team": "AA22",
                    }
          resp = app.put('/leader/1', json=payload)
          self.assertEqual(resp._status_code, 200)

   
    def test_put_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = mock_position()
        
        MockLeaderDB.methods_return = {"put": 200}
        MockLeaderDB.value_return = mock_leader()


        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.post('/leader', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_put_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 404}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = mock_position()
        
        MockLeaderDB.methods_return = {"put": 200}
        MockLeaderDB.value_return = mock_leader()


        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.post('/leader/1', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_put_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 404}
        MockPositionDB.value_return = mock_position()
        
        MockLeaderDB.methods_return = {"put": 200}
        MockLeaderDB.value_return = mock_leader()


        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.post('/leader/1', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_put_response_not_found(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = mock_position()
        
        MockLeaderDB.methods_return = {"put": 404}
        MockLeaderDB.value_return = mock_leader()

        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.put('/leader/1', json=payload)
        self.assertEqual(resp._status_code, 404)

    def test_put_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = mock_position()
        
        MockLeaderDB.methods_return = {"put": 500}
        MockLeaderDB.value_return = mock_leader()

        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        payload = {
                    "code_employee": 1001,
                    "code_position": 100,
                    "code_team": "AA22",
                  }
        resp = app.put('/leader/1', json=payload)
        self.assertEqual(resp._status_code, 500)


    def test_get_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)
        
        MockLeaderDB.methods_return = {"get": 200}
        MockLeaderDB.value_return = [mock_leader()]

        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        resp = app.get('/leader?id=1')
        self.assertEqual(resp._status_code, 200)

   
    def test_get_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)
        
        MockLeaderDB.methods_return = {"get": 400}
        MockLeaderDB.value_return = mock_leader()


        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        resp = app.get('/leader?id=1')
        self.assertEqual(resp._status_code, 400)


    def test_get_response_not_found(self):
        app = Flask(__name__)
        api = Api(app)

        MockLeaderDB.methods_return = {"get": 404}
        MockLeaderDB.value_return = mock_leader()

        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        resp = app.get('/leader?id=1')
        self.assertEqual(resp._status_code, 404)

    def test_get_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockLeaderDB.methods_return = {"get": 500}
        MockLeaderDB.value_return = mock_leader()

        api.add_resource(Leader, '/leader', '/leader/<id>', resource_class_kwargs={'db': MockConnection, 'leader_model': MockLeaderDB, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'leader_schema': LeaderSchema})

        app = app.test_client()
        resp = app.get('/leader?id=1')
        self.assertEqual(resp._status_code, 500)

if __name__ == "__main__":
    unittest.main()
    
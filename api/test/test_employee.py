from flask import Flask
from flask_restful import Api

import unittest

from controller.employee import Employee
from services.schemas import EmployeeSchema
from controller.employee import Employee

from test.mocks import MockEmployeeDB, mock_employee
from test.mocks import MockPositionDB, MockConnection


class EmployeeControllerTestCase(unittest.TestCase):
  
    def test_post_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"post": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        payload = {
                    "name":"josimar",
                    "last_name": "peixoto",
                    "code_position": 100,
                    "salary": 9000.10,
                    "password": "kklmkl",
                    "status": "ATIVO"
                  }
        resp = app.post('/employee', json=payload)
        self.assertEqual(resp._status_code, 201)


    def test_post_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"post": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 400}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        payload = {
                    "name":"josimar",
                    "last_name": "peixoto",
                    "code_position": 100,
                    "salary": 9000.10,
                    "password": "kklmkl",
                    "status": "ATIVO"
                  }
        resp = app.post('/employee', json=payload)
        self.assertEqual(resp._status_code, 400)

    def test_post_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"post": 500}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        payload = {
                    "name":"josimar",
                    "last_name": "peixoto",
                    "code_position": 100,
                    "salary": 9000.10,
                    "password": "kklmkl",
                    "status": "ATIVO"
                  }
        resp = app.post('/employee', json=payload)
        self.assertEqual(resp._status_code, 500)


    def test_get_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"get": 200}
        MockEmployeeDB.value_return = [mock_employee()]

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        resp = app.get('/employee?registration=1001')
        self.assertEqual(resp._status_code, 200)


    def test_get_response_not_found(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"get": 404}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        resp = app.get('/employee?registration=1001')
        self.assertEqual(resp._status_code, 404)

    def test_get_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"get": 500}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        resp = app.get('/employee?registration=1001')
        self.assertEqual(resp._status_code, 500)

    def test_put_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        payload = {
            "name":"josimar",
            "last_name": "peixoto",
            "code_position": 100,
            "salary": 9000.10,
            "password": "kklmkl",
            "status": "ATIVO"
            }
        resp = app.put('/employee/1001', json=payload)
        self.assertEqual(resp._status_code, 200)

    def test_put_response_not_found(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 404}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        payload = {
            "name":"josimar",
            "last_name": "peixoto",
            "code_position": 100,
            "salary": 9000.10,
            "password": "kklmkl",
            "status": "ATIVO"
            }
        resp = app.put('/employee/1001', json=payload)
        self.assertEqual(resp._status_code, 404)


    def test_put_response_not_found_code_position(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 404}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        payload = {
            "name":"josimar",
            "last_name": "peixoto",
            "code_position": 100,
            "salary": 9000.10,
            "password": "kklmkl",
            "status": "ATIVO"
            }
        resp = app.put('/employee/1001', json=payload)
        self.assertEqual(resp._status_code, 400)
    

    def test_put_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 200}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        payload = {
            "name":"josimar",
            "last_name": "peixoto",
            "code_position": 100,
            "salary": 9000.10,
            "password": "kklmkl",
            "status": "ATIVO"
            }
        resp = app.put('/employee', json=payload)
        self.assertEqual(resp._status_code, 400)
    
    def test_put_response_internal_server_error(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"put": 500}
        MockEmployeeDB.value_return = mock_employee()

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        payload = {
            "name":"josimar",
            "last_name": "peixoto",
            "code_position": 100,
            "salary": 9000.10,
            "password": "kklmkl",
            "status": "ATIVO"
            }
        resp = app.put('/employee/1001', json=payload)
        self.assertEqual(resp._status_code, 500)
    
    def test_delete_response_sucessful(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"delete": 200}
        
        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        resp = app.delete('/employee/1001')
        self.assertEqual(resp._status_code, 200)

    def test_delete_response_bad_request(self):
        app = Flask(__name__)
        api = Api(app)

        MockEmployeeDB.methods_return = {"delete": 200}
        MockEmployeeDB.value_return = [mock_employee()]

        MockPositionDB.methods_return = {"get": 200}
        MockPositionDB.value_return = {"ok":"ok"}

        api.add_resource(Employee, '/employee', '/employee/<registration>', resource_class_kwargs={'db': MockConnection, 'position_model': MockPositionDB, 'employee_model': MockEmployeeDB, 'employee_schema': EmployeeSchema})

        app = app.test_client()
        resp = app.delete('/employee')
        self.assertEqual(resp._status_code, 400)

if __name__ == "__main__":
    unittest.main()
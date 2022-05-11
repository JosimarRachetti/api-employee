from model import employee
from utils.exceptions import BadRequestException

from database.database import Employee, Position, Leader

def mock_employee():
    employee = Employee()
    employee.name = "josimar"
    employee.last_name = "rachetti"
    employee.salary = "8000"
    employee.status = "ATIVO"
    employee.registration = 1001
    employee.code_position = 100
    employee.password = "fdfasd"
    employee.last_update = "01/01/2022"
    employee.create = "01/01/2022"
    return employee

def mock_position():
    position = Position()
    position.id = 100
    position.title = "analista desenvolvimento"
    position.code_team = "AAS2"
    position.description = "desenvolver e testar api"
    position.create = "01/01/2020"
    position.last_update = "01/01/2020"
    position.status = "ABERTA"
    return position

def mock_leader():
    leader = Leader()
    leader.id = 1
    leader.code_employee = 1001
    leader.code_position = 101
    leader.code_team = "AA2S"
    leader.create = "01/01/2020"
    return leader
    
class MockDB:
    def __init__(self):
        pass 

    def value_to_return(self, value, value_return):
        if value == 200:
            return value_return
        if value == 400:
            raise BadRequestException('bad request')
        if value == 404:
            return []
        if value == 500:
            raise Exception('internal error')


class MockEmployeeDB(MockDB):
    methods_return = {}
    value_return = {}
    def __init__(self, db):
        super().__init__()

    def new_employee(self, **data):
        return self.value_to_return(self.methods_return.get("post", 200), self.value_return)

    def update_employee(self, **data):
        return self.value_to_return(self.methods_return.get("put", 200), self.value_return)

    def find_employee(self, **query):
        return self.value_to_return(self.methods_return.get("get", 200), self.value_return)
       
    def delete_employee(self, **query):
        return self.value_to_return(self.methods_return.get("delete", 200), self.value_return)

class MockPositionDB(MockDB):
    methods_return = {}
    value_return = {}
    def __init__(self, db):
        super().__init__()

    def new_position(self, **data):
        return self.value_to_return(self.methods_return.get("post", 200), self.value_return)

    def update_position(self, **data):
        return self.value_to_return(self.methods_return.get("put", 200), self.value_return)

    def find_position(self, **query):
        return self.value_to_return(self.methods_return.get("get", 200), self.value_return)
       
    def delete_position(self, **query):
        return self.value_to_return(self.methods_return.get("delete", 200), self.value_return)

class MockLeaderDB(MockDB):
    methods_return = {}
    value_return = {}
    def __init__(self, db):
        super().__init__()

    def new_leader(self, **data):
        return self.value_to_return(self.methods_return.get("post", 200), self.value_return)

    def update_leader(self, **data):
        return self.value_to_return(self.methods_return.get("put", 200), self.value_return)

    def find_leader(self, **query):
        return self.value_to_return(self.methods_return.get("get", 200), self.value_return)
       
    def delete_leader(self, **query):
        return self.value_to_return(self.methods_return.get("delete", 200), self.value_return)


class MockConnection:
    def __init__(self):
        pass
    def create_session(self):
        return SessionDb()

class SessionDb:
    def __init__(self) -> None:
        pass

    def commit(self):
        return 'TESTE'

    def rollback(self):
        return 'TESTE'
    
    def close(self):
        return 'TESTE'
        
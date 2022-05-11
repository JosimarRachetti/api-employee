from database.database import Employee
from model.base import BaseDb
from datetime import datetime


class EmployeeDB(BaseDb):
    def __init__(self, db):
        super().__init__()
        self.db = db

    def new_employee(self, **data):
        employee = Employee()
        employee = self.set_values(employee, **data)
        employee = self.add_db(employee)
        return employee


    def update_employee(self, **data):
        employee_to_update = self.find_employee(**{"registration": int(data['registration'])})
        if not len(employee_to_update) > 0:
            return employee_to_update
        data = {**data, "last_update": str(datetime.now().isoformat())}
        employee_already_updated = self.update_db(employee_to_update[0], **data)
        return employee_already_updated

    def find_employee(self, **query):
        query = self.build_query(Employee, **query)
        return query.all()
       
    def delete_employee(self, **query):
        query = self.build_query(Employee, **query)
        self.delete_db(query)
        return 

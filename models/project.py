from models.assignment_server import Assignment_Server
from models.task import Task
from models.employee import Employee

class Project:
    def __init__(self, id, name, desc, tasks = None, emp = None):
        self.id = id
        self.name = name
        self.description = desc
        self.tasks = set(tasks) if tasks else set()
        self.employees = set(emp) if tasks else set()
        self.assignment_server = Assignment_Server(emp, tasks)

    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        self.tasks.add(task)
        self.assignment_server.add_task(task)

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be added.")
        self.employees.add(employee)
        self.assignment_server.add_employee(employee)
    

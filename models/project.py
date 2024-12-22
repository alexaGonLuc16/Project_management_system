from models.assignment_server import Assignment_Server

class Project:
    def __init__(self, id, name, desc, tasks = None, emp = None):
        self.id = id
        self.name = name
        self.description = desc
        self.tasks = set(tasks) if tasks else set()
        self.employees = set(emp) if tasks else set()
        self.assignment_server = Assignment_Server(emp, tasks)

    def add_task(self, task):
        self.tasks.add(task)
        self.assignment_server.add_task(task)

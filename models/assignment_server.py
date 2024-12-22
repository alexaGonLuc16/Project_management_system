from models.task import Task
from models.employee import Employee

class Assignment_Server:
    def __init__(self, employees = None, tasks = None):
        self.assignments = {} #key: task, value: employee
        self.tasks = set(tasks) if tasks else set()            #object array
        self.employees = set(employees) if employees else set()    #object array
    
    #get_assigned_employees of a task
    def get_assigned_employees(self, id_task):
        return self.assignments[id_task]

    def add_task(self, task): 
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        self.tasks.add(task)    
    
    def get_matching_employees(self, task):
        if not isinstance(task, Task):
            raise TypeError("Argument must be a Task object.")
        
        matching_employees = {} #key: id_employee, value: set with matching skills
        for emp in self.employees:
            if not isinstance(emp, Employee):
                    raise TypeError("Argument must be a Employee object.")
            if task.technologies_used & emp.skills:
                matching_employees [emp.id] = task.technologies_used & emp.skills

        return matching_employees
    #def assign_all_tasks():
    #pending to design an algorith for task assignment 

    


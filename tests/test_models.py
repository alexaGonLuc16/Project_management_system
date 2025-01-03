import unittest 
from models import Employee, Task, Assignment_Server, Project

class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        employee = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        self.assertEqual(employee.id, 1)
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.skills, {"Python", "Django"})

    def test_add_project_to_employee(self):
        employee = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        task = Task(id=1, id_proj=1, name="Task1", tech_used={"Python"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        project = Project(id=1, name="Project1", desc="Project Description", tasks = {task}, emp = {employee})

        employee.add_project(project.id, tasks = [task.id])
        self.assertIn(project.id, employee.projects)
        self.assertIn(task.id, employee.projects[project.id])

    def test_get_num_tasks(self):
        employee = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        task = Task(id=1, id_proj=1, name="Task1", tech_used={"Python"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        project = Project(id=1, name="Project1", desc="Project Description", tasks = {task}, emp = {employee})
        employee.add_project(project.id, tasks = {task})
        num_tasks = 1
        self.assertEqual(num_tasks, employee.get_num_tasks())

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task(id=1, id_proj=1, name="Task1", tech_used={"Python"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        self.assertEqual(task.name, "Task1")
        self.assertEqual(task.technologies_used, {"Python"})
        self.assertEqual(task.deadline, "2024-12-31")

class TestProject(unittest.TestCase):
    def test_project_creation(self):
        project = Project(id=1, name="Project1", desc="Project Description")
        self.assertEqual(project.name, "Project1")
        self.assertEqual(project.description, "Project Description")

    def test_add_task_to_project(self):
        project = Project(id=1, name="Project1", desc="Project Description")
        task = Task(id=1, id_proj=1, name="Task1", tech_used={"Python"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        project.add_task(task)
        self.assertIn(task, project.tasks)

    def test_add_employee_to_project(self):
        project = Project(id=1, name="Project1", desc="Project Description")
        employee = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        employee2 = Employee(id=1, name="Joha Ju", skills={"Python", "Django", "React"})
        project.add_employee(employee)
        project.add_employee(employee2)
        self.assertIn(employee, project.employees)

class TestAssignmentServer(unittest.TestCase):
    def test_add_task(self):
        project = Project(id=1, name="Project1", desc="Project Description")
        assignment_server = Assignment_Server(project.id)
        task = Task(id=1, id_proj=1, name="Task1", tech_used={"Python"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        assignment_server.add_task(task)
        self.assertIn(task, assignment_server.tasks)

    def test_add_employee(self):
        project = Project(id=1, name="Project1", desc="Project Description")
        assignment_server = Assignment_Server(project.id)
        employee = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        assignment_server.add_employee(employee)
        self.assertIn(employee, assignment_server.employees)

    def test_get_matching_employees(self):
        project = Project(id=1, name="Project1", desc="Project Description")
        employee1 = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        employee2 = Employee(id=2, name="Jane Smith", skills={"Java", "Spring"})
        task = Task(id=1, id_proj=1, name="Task1", tech_used={"Python","SQL"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        
        assignment_server = Assignment_Server(project.id, employees=[employee1, employee2], tasks = [task])
        matching_employees = assignment_server.get_matching_employees(task)
        
        self.assertEqual(matching_employees[employee1.id], {"Python"})
        self.assertNotIn(employee2.id, matching_employees)
    
    #this test is not ready
    def test_assign_all_tasks(self):
        project = Project(id=1, name="Project1", desc="Project Description")
        employee1 = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        employee1.add_project(project.id)
        employee2 = Employee(id=2, name="Jane Smith", skills={"Java", "Spring"})
        employee2.add_project(project.id)
        employee3 = Employee(id=3, name="Adam Jones", skills={"C++", "Python","SQL"})
        employee3.add_project(project.id)
        task1 = Task(id=1, id_proj=1, name="Task1", tech_used={"Python","SQL"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        task2 = Task(id=2, id_proj=1, name="Task2", tech_used={"Java","Spring"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=1)
        assignment_server = Assignment_Server(project.id, employees=[], tasks = [task1,task2])
        assignment_server.add_employee(employee1)
        assignment_server.add_employee(employee2)
        assignment_server.add_employee(employee3)
        assignment_server.assign_all_tasks()

if __name__ == '__main__':
    unittest.main()
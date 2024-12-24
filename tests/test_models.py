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

        employee.add_project(project, tasks = {task})
        self.assertIn(project, employee.projects)
        self.assertIn(task, employee.projects[project])

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
        project.add_employee(employee)
        self.assertIn(employee, project.employees)

class TestAssignmentServer(unittest.TestCase):
    def test_add_task(self):
        assignment_server = Assignment_Server()
        task = Task(id=1, id_proj=1, name="Task1", tech_used={"Python"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        assignment_server.add_task(task)
        self.assertIn(task, assignment_server.tasks)

    def test_add_employee(self):
        assignment_server = Assignment_Server()
        employee = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        assignment_server.add_employee(employee)
        self.assertIn(employee, assignment_server.employees)

    def test_get_matching_employees(self):
        employee1 = Employee(id=1, name="John Doe", skills={"Python", "Django"})
        employee2 = Employee(id=2, name="Jane Smith", skills={"Java", "Spring"})
        task = Task(id=1, id_proj=1, name="Task1", tech_used={"Python"}, desc="Task description", stat="Pending", deadline="2024-12-31", emp_needed=2)
        
        assignment_server = Assignment_Server(employees=[employee1, employee2], tasks = [task])
        matching_employees = assignment_server.get_matching_employees(task)
        
        self.assertEqual(matching_employees[employee1.id], {"Python"})
        self.assertNotIn(employee2.id, matching_employees)

if __name__ == '__main__':
    unittest.main()
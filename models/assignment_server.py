from models.task import Task
from models.employee import Employee

class Assignment_Server:
    def __init__(self, id_project, employees=None, tasks=None):
        self.id_project = id_project
        # List of assignment dictionaries; each dictionary represents a task with key: skill, value: employee ID
        self.assignments = []
        # Maps each skill to a list of employee IDs who possess that skill
        self.emp_per_skill = {}
        # List of skills sorted by the number of employees who have them (ascending order)
        self.ranked_skills = []
        # Maps employee IDs to Employee objects
        self.employee_map = {emp.id: emp for emp in employees} if employees else {}
        # Maps task IDs to Task objects
        self.task_map = {task.id: task for task in tasks} if tasks else {}
        # Tracks the number of tasks each employee is assigned to
        self.emp_checking = {emp.id: 0 for emp in employees} if employees else {}

    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        self.task_map[task.id] = task  # Add new task to the task map

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be added.")
        self.employee_map[employee.id] = employee  # Add new employee to the employee map
        # Update skill-to-employee mapping
        for skill in employee.skills:
            if skill in self.emp_per_skill:
                self.emp_per_skill[skill].append(employee.id)
        self.emp_checking[employee.id] = 0  # Initialize task assignment count for the new employee

    def count_skills(self):
        # Ensure all required technologies are keys in emp_per_skill
        for task in self.task_map.values():
            for tech in task.technologies_used:
                if tech not in self.emp_per_skill:
                    self.emp_per_skill[tech] = []
        # Map employees to their respective skills
        for emp in self.employee_map.values():
            for skill in emp.skills:
                if skill in self.emp_per_skill:
                    self.emp_per_skill[skill].append(emp.id)

    def rank_skills(self):
        # Rank skills based on the number of employees possessing them (ascending order)
        self.ranked_skills = sorted(
            self.emp_per_skill.keys(),
            key=lambda skill: len(self.emp_per_skill[skill])
        )

    def prioritize_tasks(self):
        # Sort tasks by their priority attribute (lower value indicates higher priority)
        tasks_per_priority = sorted(
            self.task_map.keys(),
            key=lambda id: self.task_map[id].priority
        )
        return tasks_per_priority

    def assign_all_tasks(self):
        tasks_per_priority = self.prioritize_tasks()  # List of task IDs ordered by priority
        self.count_skills()  # Map employees to skills
        self.rank_skills()   # Rank skills based on employee availability

        for i, task_id in enumerate(tasks_per_priority):
            self.assignments.append({})  # Initialize assignment dictionary for the current task
            task_skill_checking = {}     # Track which skills have been assigned for the current task
            task_ranked_skills = []      # Skills required by the task, ordered by global skill ranking
            # Identify and rank skills required for the task
            for skill in self.ranked_skills:
                if skill in self.task_map[task_id].technologies_used:
                    task_ranked_skills.append(skill)
                    task_skill_checking[skill] = 0  # Mark skill as unassigned

            # Assign employees to each required skill
            for skill,_ in task_skill_checking.items():
                if task_skill_checking[skill] == 0:
                    emp_id_aux = 0
                    for emp_id in self.emp_per_skill[skill]:
                        if self.emp_checking[emp_id] < 2:  # Limit of 2 tasks per employee
                            self.assignments[i][skill] = emp_id  # Assign employee to skill
                            emp_id_aux = emp_id

                            if emp_id_aux != 0:
                                task_skill_checking[skill] = 1  # Mark skill as assigned
                                # Remove the assigned skill from the skill list
                                task_ranked_skills.remove(skill)
                                self.emp_checking[emp_id_aux] += 1

                                # Assign additional skills if the employee has other matching technologies
                                if (
                                    self.emp_checking[emp_id_aux] == 1
                                    and self.task_map[task_id].technologies_used & set(task_ranked_skills)
                                ):
                                    matching_skills = self.task_map[task_id].technologies_used & set(task_ranked_skills)
                                    additional_skill = next(iter(matching_skills))
                                    self.assignments[i][additional_skill] = emp_id_aux  # Assign additional skill
                                    task_skill_checking[additional_skill] = 1  # Mark as assigned
                                    # Remove the assigned skill from the skill list
                                    task_ranked_skills.remove(additional_skill) 
                                    self.emp_checking[emp_id_aux] += 1
                            break
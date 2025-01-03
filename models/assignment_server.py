from models.task import Task
from models.employee import Employee
import heapq

# Create priority queue for skills ranking
priority_skills = []

class Assignment_Server:
    def __init__(self, id_project, employees = None, tasks = None):
        self.id_project = id_project
        self.assignments = {} #key: task, value: employees -> technologies
        self.tasks = set(tasks) if tasks else set()            #object array
        self.employees = set(employees) if employees else set()    #object array
        self.ranked_skills = {} #skills hashmap 
        self.employee_map = {emp.id: emp for emp in self.employees}
        self.task_map = {task.id: task for task in self.tasks}

    def add_task(self, task): 
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        self.tasks.add(task)    

    def add_employee(self, employee): 
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be added.")
        self.employees.add(employee)    
        for skill in employee.skills:
            if skill in self.ranked_skills:
                self.ranked_skills[skill] += 1
            else:
                self.ranked_skills[skill] = 1              
     
    def get_matching_employees(self, task):
        if not isinstance(task, Task):
            raise TypeError("Argument must be a Task object.")
        
        matching_employees = {} #key: id_employee, value: set with matching skills
        for emp in self.employees:
            if not isinstance(emp, Employee):
                    raise TypeError("Argument must be a Employee object.")
            if task.technologies_used & emp.skills:
                matching_employees[emp.id] = task.technologies_used & emp.skills

        return matching_employees
    
    def assign_all_tasks(self):
        print("Contenido inicial de ranked_skills:", self.ranked_skills)
        #dictionary for employee asignment
        employee_checking = {}
        for emp in self.employees:
            if not isinstance(emp, Employee):
                raise TypeError(f"Expected Employee object, but got {type(emp)}")
            employee_checking[emp.id] = False

        for task in self.tasks:    
            if not isinstance(task, Task):
                raise TypeError("Expected Task object in tasks set.")
            map_employees = {} #employees per technology

            for tech in task.technologies_used:
                #list of skills to manage employee assingment               
                if tech in self.ranked_skills:
                    map_employees[tech] = set()
                
            #build checking for skills needed
            skills_checking = {tech: 0 for tech in task.technologies_used}

            # Build priority queue based on ranked_skills
            priority_skills = [(self.ranked_skills[tech], tech) for tech in task.technologies_used if tech in self.ranked_skills]
            heapq.heapify(priority_skills)
            skills_check_set = {skill for _, skill in priority_skills}

            matching = self.get_matching_employees(task)
            if matching:
                print("\nTask id: ", task.id)
                print("Matching skills of employees: ", matching)
            else:
                print("Missing employees for task: ", task.id)
            print("Skill top: ", priority_skills[0])

            for emp_id, _ in matching.items():
                emp = next(e for e in self.employees if e.id == emp_id)  # Retrieve the object
                if not isinstance(emp, Employee):
                    raise TypeError(f"Expected Employee object, but got {type(emp)}")
            
                if priority_skills[0][1] in skills_check_set and priority_skills[0][1] in matching[emp_id] and emp.get_num_tasks() <= 2:
                    self.assignments[task.id] = {}
                    self.assignments[task.id][emp.id] = [priority_skills[0][1]]
                     # Ensure that the project exists in emp.projects and is a set
                    if self.id_project not in emp.projects:
                        emp.projects[self.id_project] = set()  # Initialize as an empty set if the project is not present
                        
                    if len(emp.projects[self.id_project]) == 0 : 
                        emp.projects[self.id_project].add(task.id) #assign task to employee
                        print("employee: ", emp.id, "assigned to ")
                        print("task ", emp.projects[self.id_project] ,"of project: ", self.id_project)
                        matching[emp_id].remove(priority_skills[0][1])
                        skills_checking[priority_skills[0][1]] = emp_id
                        print("Current skills checking: ", priority_skills[0][1]," -> ", skills_checking[priority_skills[0][1]])
                        skills_check_set.remove(priority_skills[0][1])
                        heapq.heappop(priority_skills)#delete top element
                        heapq.heapify(priority_skills)

                        if len(matching[emp_id]) > 0 and next(iter(matching[emp_id])) in skills_check_set:
                            print("This employee has one more skill to assign")
                            #assign one more technology to the employee
                            if skills_checking[next(iter(matching[emp_id]))] == 0:
                                skills_checking[next(iter(matching[emp_id]))] = emp_id
                                skills_check_set.remove(next(iter(matching[emp_id])))

                    print("skill assignment: ",  skills_checking)
                else:
                    heapq.heappop(priority_skills)
                    heapq.heapify(priority_skills)


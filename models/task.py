class Task:
    def __init__(self, id, id_proj, name, tech_used, desc, stat, deadline, emp_needed): 
        self.id = id    
        self.id_project = id_proj
        self.name = name
        self.technologies_used = set(tech_used) #set structure
        self.description = desc
        self.status = stat
        self.deadline = deadline
        self.employees_needed = emp_needed

    
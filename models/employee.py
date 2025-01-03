class Employee:
    def __init__(self, id, name, skills = None):
        self.id = id
        self.name = name
        self.skills = set(skills) if skills else set() #set structure
        self.projects = {}  # Dictionary

    def add_project(self, project_id, tasks = None):
        self.projects[project_id] = set(tasks) if tasks else set()

    def get_num_tasks(self):
        num_tasks = 0
        for project in self.projects:
            num_tasks += len(self.projects[project])
        
        return num_tasks
    
        




    

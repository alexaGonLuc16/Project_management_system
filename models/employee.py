class Employee:
    def __init__(self, id, name, skills = None, projects = None):
        self.id = id
        self.name = name
        self.skills = set(skills) if skills else set() #set structure
        self.projects = projects if projects else {}  # Dictionary

    def add_project(self, project, tasks = None):
        self.projects[project] = set(tasks) if tasks else set()

    
        




    

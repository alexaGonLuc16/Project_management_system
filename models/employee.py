class Employee:
    def __init__(self, id, name, skills = None):
        self.id = id
        self.name = name
        self.skills = set(skills) if skills else set() #set structure
        self.projects = {}  # Dictionary key: id project, val: set of tasks assigned(id)

    def add_project(self, project_id, tasks = None):
        self.projects[project_id] = set(tasks) if tasks else set()

    def get_num_tasks(self):
        num_tasks = 0
        for project in self.projects:
            num_tasks += len(self.projects[project])
        return num_tasks
    
    def set_task(self, id_project, id_task):
        if id_task not in self.projects[id_project]:
            self.projects[id_project].add(id_task)
            return 1 #task added succesfully
        else:
            return 0 #task already existing
        




    

class Project():
    def __init__(self, project):
        self.project = project

    def get_project(self):
        print(self.project)

my_vpsproject = Project("BT-Unilever, TVC and VPS")
my_vpsproject.get_project()
my_project2 = Project (" Dynatech")
my_project2.get_project()

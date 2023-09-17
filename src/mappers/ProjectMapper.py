from src.models.Project import Project

class ProjectMapper:
    @staticmethod
    def fromJsontoProject(pojectJson):
        return Project(pojectJson).__dict__

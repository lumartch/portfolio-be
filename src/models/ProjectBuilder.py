from src.models.Project import Project
from src.util.Enums import EGitSource

class ProjectBuilder(Project):
    
    def __init__(self):
        self.project = Project()

    def set_source(self, source: EGitSource):
        self.project.source = source.value
        return self

    def get_project(self):
        return self.project
    
    def set_id(self, id:int):
        self.project.id = id
        return self
    
    def set_name(self, name:str):
        self.project.name = name
        return self
    
    def set_full_name(self, full_name:str):
        self.project.full_name = full_name
        return self
    
    def set_html_url(self, html_url:str):
        self.project.html_url = html_url
        return self
    
    def set_archived(self, archived:bool):
        self.project.archived = archived
        return self
    
    def set_git_url(self, git_url:str):
        self.project.git_url = git_url
        return self
    
    def set_ssh_url(self, ssh_url:str):
        self.project.ssh_url = ssh_url
        return self
    
    def set_clone_url(self, clone_url:str):
        self.project.clone_url = clone_url
        return self
    
    def set_svn_url(self, svn_url:str):
        self.project.svn_url = svn_url
        return self
    
    def set_default_branch(self, default_branch:str):
        self.project.default_branch = default_branch
        return self
    
    def set_created_at(self, created_at:str):
        self.project.created_at = created_at
        return self
from src.models.ProjectBuilder import ProjectBuilder
from src.util.Enums import EGitSource

class ProjectMapper:
    @staticmethod
    def fromGitHubtoProject(json: object):
        projectBuilder = ProjectBuilder()
        projectBuilder.set_source(EGitSource.GIT_HUB).set_id(json['id']).set_name(json['name']).set_full_name(json['full_name'])
        projectBuilder.set_html_url(json['html_url']).set_archived(json['archived']).set_git_url(json['git_url'])
        projectBuilder.set_ssh_url(json['ssh_url']).set_clone_url(json['clone_url']).set_svn_url(json['svn_url'])
        projectBuilder.set_default_branch(json['default_branch']).set_created_at(json['created_at'])
        return projectBuilder.get_project().__dict__
    
    @staticmethod
    def fromGitlabtoProject(json: object, archived: bool = False):
        projectBuilder = ProjectBuilder()
        projectBuilder.set_source(EGitSource.GIT_LAB).set_id(json['id']).set_name(json['name']).set_full_name(json['path_with_namespace'])
        projectBuilder.set_html_url(json['web_url']).set_archived(archived).set_git_url(json['http_url_to_repo'])
        projectBuilder.set_ssh_url(json['ssh_url_to_repo'])
        projectBuilder.set_default_branch(json['default_branch']).set_created_at(json['created_at'])
        return projectBuilder.get_project().__dict__

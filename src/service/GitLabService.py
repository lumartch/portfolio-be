import json
from flask import abort
import requests

from src.util.Enums import EGitLab
from src.util.Enums import EGitSource
from src.models.Profile import Profile
from src.mappers.ProjectMapper import ProjectMapper
from src.mappers.ProfileMapper import ProfileMapper
from src.util.ErrorMessageFormatter import notFoundUsername

class GitLabService():
    profile_uri = EGitLab.GITLAB_BASE_URI.value + EGitLab.USER.value
    repos_uri = EGitLab.GITLAB_BASE_URI.value + EGitLab.REPOS.value
    def getGitlabProfile(self, username: str):
        profile_uri = self.profile_uri.replace('{username}', username)
        try:
            response = requests.get(url = profile_uri)
            if response.status_code == 404 or response.json() == []:
                abort(404, notFoundUsername(username, git_source=EGitSource.GIT_LAB))
            profile = json.loads(json.dumps(ProfileMapper.fromGitlabToProfile(response.json()[0] )))
            return profile
        # except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
        # except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    
    def getGitlabRepos(self, username: str, archived: bool = False):
        repos_uri = self.repos_uri.replace('{username}', username)
        params = { "archived": archived }
        try:
            response = requests.get(url = repos_uri, params=params).text
            projects = list(map( lambda entry: ProjectMapper.fromGitlabtoProject(json=entry, archived=archived), json.loads(response)))
            return projects
        # except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
        # except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
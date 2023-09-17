import json
from flask import abort
import requests
from src.util.Enums import EGitHub
from src.models.Profile import Profile
from src.mappers.ProjectMapper import ProjectMapper
from src.util.ErrorMessageFormatter import notFoundUsername


class GitHubService():
    profile_uri = EGitHub.GITHUB_BASE_URI.value + EGitHub.USER.value
    repos_uri = EGitHub.GITHUB_BASE_URI.value + EGitHub.REPOS.value
    def getGithubProfile(self, username):
        profile_uri = self.profile_uri.replace('{username}', username)
        try:
            response = requests.get(url = profile_uri)
            if response.status_code == 404:
                abort(404, notFoundUsername(username))
            profile = json.loads(json.dumps(Profile(response.json()).__dict__))
            return profile
        # except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
        # except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    
    def getGithubRepos(self, username, archived):
        repos_uri = self.repos_uri.replace('{username}', username)
        try:
            response = requests.get(url = repos_uri).text
            projects = list(filter(lambda project: project['archived'] == archived, map(ProjectMapper.fromJsontoProject, json.loads(response))))
            return projects
        # except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
        # except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
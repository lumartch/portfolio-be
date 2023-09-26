import json
from flask import Flask
from flask_cors import CORS
from flask_caching import Cache
from werkzeug.exceptions import HTTPException
from flask_parameter_validation import ValidateParameters, Route, Query

from src.util.Enums import *
from src.service.GitHubService import GitHubService
from src.service.GitLabService import GitLabService

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
app = Flask(__name__)
CORS(app)
cache.init_app(app)

BASE_API_URI = EApiPaths.BASE_API_URI.value + EApiPaths.USER.value + EApiPaths.PATH_PARAM_USER.value
github_service = GitHubService()
gitlab_service = GitLabService()

@app.get(BASE_API_URI + EApiPaths.INFO.value)
@cache.cached(timeout=120)
@ValidateParameters()
def getUser(username: str = Route(), git_source: str = Query(EGitSource.ALL.value)):
    if(git_source == EGitSource.GIT_HUB.value):
        return github_service.getGithubProfile(username=username)
    elif(git_source == EGitSource.GIT_LAB.value):
        return gitlab_service.getGitlabProfile(username=username)
    else:
        github_profile = github_service.getGithubProfile(username=username)
        gitlab_profile = gitlab_service.getGitlabProfile(username=username)
        profile = {
            EGitSource.GIT_HUB.value: github_profile,
            EGitSource.GIT_LAB.value: gitlab_profile
        }
        return profile

@app.get(BASE_API_URI + EApiPaths.REPOS.value)
@cache.cached(timeout=120)
@ValidateParameters()
def getRepos(username: str = Route(), archived: bool = Query(False), git_source: str = Query(EGitSource.ALL.value)):
    if(git_source == EGitSource.GIT_HUB.value):
        return github_service.getGithubRepos(username=username, archived=archived)
    elif(git_source == EGitSource.GIT_LAB.value):
        return gitlab_service.getGitlabRepos(username=username, archived=archived)
    else:
        github_repos = github_service.getGithubRepos(username=username, archived=archived)
        gitlab_repos = gitlab_service.getGitlabRepos(username=username, archived=archived)
        return github_repos + gitlab_repos

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
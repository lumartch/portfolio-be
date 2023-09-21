from flask import Flask, request, abort
from werkzeug.exceptions import HTTPException
from flask_parameter_validation import ValidateParameters, Route, Json, Query

import json
from src.util.Enums import *
from src.service.GitHubService import GitHubService
from src.service.GitLabService import GitLabService

app = Flask(__name__)
BASE_API_URI = EApiPaths.BASE_API_URI.value + EApiPaths.USER.value + EApiPaths.PATH_PARAM_USER.value
github_service = GitHubService()
gitlab_service = GitLabService()

@app.get(BASE_API_URI + EApiPaths.INFO.value)
@ValidateParameters()
def getUser(username: str = Route()):
    return github_service.getGithubProfile(username=username)

@app.get(BASE_API_URI + EApiPaths.REPOS.value)
@ValidateParameters()
def getRepos(username: str = Route(), archived: bool = Query(False)):
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
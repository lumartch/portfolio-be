from flask import Flask

from src.util.Enums import *
from src.service.GitHubService import GitHubService

app = Flask(__name__)
BASE_API_URI = EApiPaths.BASE_API_URI.value + EApiPaths.USER.value + EApiPaths.PATH_PARAM_USER.value
github_service = GitHubService()

@app.route(BASE_API_URI + EApiPaths.INFO.value)
def getUser(username):
    return github_service.getGithubProfile(username=username)

@app.route(BASE_API_URI + EApiPaths.REPOS.value)
def getRepos(username):
    return github_service.getGithubRepos(username=username)
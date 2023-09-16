from flask import Flask
import requests

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
    uri = EGitHub.GITHUB_BASE_URI.value + EGitHub.REPOS.value.replace('{username}', username)
    r = requests.get(url = uri)
    return r.json()
from flask import Flask
import requests

from src.util.Enums import *

app = Flask(__name__)
BASE_API_URI = EApiPaths.BASE_API_URI.value + EApiPaths.USER.value + EApiPaths.PATH_PARAM_USER.value

@app.route(BASE_API_URI + EApiPaths.INFO.value)
def getUser(username):
    uri = EGitHub.GITHUB_BASE_URI.value + EGitHub.USER.value.replace('{username}', username)
    r = requests.get(url = uri)
    return r.json()

@app.route(BASE_API_URI + EApiPaths.REPOS.value)
def getRepos(username):
    uri = EGitHub.GITHUB_BASE_URI.value + EGitHub.REPOS.value.replace('{username}', username)
    r = requests.get(url = uri)
    return r.json()
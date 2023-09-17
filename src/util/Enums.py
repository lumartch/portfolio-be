from enum import Enum

class EGitHub(Enum):
    GITHUB_BASE_URI = 'https://api.github.com'
    USER = '/users/{username}'
    REPOS = '/users/{username}/repos'
    STARRED_REPOS = '/users/{username}/starred'

class EApiPaths(Enum):
    BASE_API_URI = '/api'
    PATH_PARAM_USER = '/<string:username>'
    USER = '/user'
    INFO = '/info'
    REPOS = '/repos'

class EErrorMessages(Enum):
    INVALID_USERNAME = "Username '{username}' not found in Github."
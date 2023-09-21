from enum import Enum

class EGitHub(Enum):
    GITHUB_BASE_URI = 'https://api.github.com'
    USER = '/users/{username}'
    REPOS = '/users/{username}/repos'
    STARRED_REPOS = '/users/{username}/starred'

class EGitLab(Enum):
    GITLAB_BASE_URI = "https://gitlab.com/api/v4"
    USER = '/users?username={username}'
    REPOS = '/users/{username}/projects'

class EGitSource(Enum):
    GIT_HUB = 'github'
    GIT_LAB = 'gitlab'

class EApiPaths(Enum):
    BASE_API_URI = '/api'
    PATH_PARAM_USER = '/<string:username>'
    USER = '/user'
    INFO = '/info'
    REPOS = '/repos'

class EErrorMessages(Enum):
    USERNAME_NOT_FOUND = "Username '{username}' not found in Github."
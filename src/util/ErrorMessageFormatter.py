from src.util.Enums import EErrorMessages
from src.util.Enums import EGitSource

def notFoundUsername(username: str, git_source: EGitSource):
    return EErrorMessages.USERNAME_NOT_FOUND.value.replace('{username}', username).replace('{git_source}', git_source.value)
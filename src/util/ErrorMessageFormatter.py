from src.util.Enums import EErrorMessages

def notFoundUsername(username):
    return EErrorMessages.USERNAME_NOT_FOUND.value.replace('{username}', username)
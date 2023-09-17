from src.util.Enums import EErrorMessages

def notFoundUsername(username):
    return EErrorMessages.INVALID_USERNAME.value.replace('{username}', username)
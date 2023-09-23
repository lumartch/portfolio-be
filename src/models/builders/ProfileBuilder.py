from src.models.Profile import Profile
from src.util.Enums import EGitSource

class ProfileBuilder(Profile):
    
    def __init__(self):
        self.profile = Profile()

    def set_source(self, source: EGitSource):
        self.profile.source = source.value
        return self

    def get_profile(self):
        return self.profile
    
    def set_user_id(self, user_id: int):
        self.profile.user_id = user_id
        return self
    
    def set_name(self, name: str):
        self.profile.name = name
        return self
    
    def set_username(self, username: str):
        self.profile.username = username
        return self
    
    def set_email(self, email: str):
        self.profile.email = email
        return self
    
    def set_git_uri(self, git_uri: str):
        self.profile.git_uri = git_uri
        return self
    
    def set_avatar_uri(self, avatar_uri: str):
        self.profile.avatar_uri = avatar_uri
        return self
    
    def set_bio(self, bio:str):
        self.profile.bio = bio
        return self
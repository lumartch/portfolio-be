from src.models.builders.ProfileBuilder import ProfileBuilder

class ProfileMapper:
    @staticmethod
    def fromGithubToProfile(json: object):
        profileBuilder = ProfileBuilder()
        profileBuilder.set_user_id(json['id']).set_name(json['name']).set_username(json['login'])
        profileBuilder.set_email(json['email']).set_git_uri(json['html_url']).set_avatar_uri(json['avatar_url']).set_bio(json['bio'])
        return profileBuilder.get_profile().__dict__
    
    @staticmethod
    def fromGitlabToProfile(json: object):
        profileBuilder = ProfileBuilder()
        profileBuilder.set_user_id(json['id']).set_name(json['name']).set_username(json['username'])
        profileBuilder.set_git_uri(json['web_url']).set_avatar_uri(json['avatar_url'])
        return profileBuilder.get_profile().__dict__
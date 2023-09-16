class Profile:
    user_id = 0
    name= ''
    login = ''
    email = ''
    avatar_uri = ''
    github_uri = ''
    bio = ''
    def __init__(self, json):
        self.user_id = json['id']
        self.email = json['email']
        self.name = json['name']
        self.login = json['login']
        self.avatar_uri = json['avatar_url']
        self.bio = json['bio']
        self.github_uri = json['html_url']
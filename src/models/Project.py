class Project:
    id: 0
    name= ""
    full_name = ""
    html_url = ""
    archived = False
    git_url = ""
    ssh_url = ""
    clone_url = ""
    svn_url = ""
    homepage = ""
    contributors_url = ""
    default_branch = ""
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.full_name = json['full_name']
        self.html_url = json['html_url']
        self.archived = json['archived']
        self.git_url = json['git_url']
        self.ssh_url = json['ssh_url']
        self.clone_url = json['clone_url']
        self.svn_url = json['svn_url']
        self.homepage = json['homepage']
        self.contributors_url = json['contributors_url']
        self.default_branch = json['default_branch']
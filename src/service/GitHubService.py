import json
import requests
from src.util.Enums import EGitHub
from src.models.Profile import Profile


class GitHubService():
    profile_uri = EGitHub.GITHUB_BASE_URI.value + EGitHub.USER.value
    def getGithubProfile(self, username):
        profile_uri = self.profile_uri.replace('{username}', username)
        try:
            response = requests.get(url = profile_uri)
            profile = json.loads(json.dumps(Profile(response.json()).__dict__))
            return profile
        # except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
        # except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)
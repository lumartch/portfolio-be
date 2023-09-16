from flask import Flask

app = Flask(__name__)

@app.route("/api/user/<username>/info")
def getUser(username):
    return { "usermane": username }

@app.route("/api/user/<username>/repos")
def getRepos(username):
    return { "usermane": username, "repos": "repositorios" }
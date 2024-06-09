from flask import Flask

app = Flask(__name__)

milwaukee_team = ["Giannis", "Lillard", "Middleton", "Brook Lopez"]

# https://localhost:5000/

@app.route("/")
def index():
    return "<h1>Main Title</h1><p>This is the main page</p>"

@app.route("/hello")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/team", methods = ["GET"])
def reasons_to_love_my_kitten():
    return milwaukee_team

@app.route("/team/<index>", methods = ["GET"])
def add_reason(index):
    return milwaukee_team[int(index)]

@app.route("/delete_athlete/<int:index>", methods = ["GET", "DELETE"])
def delete_athlete(index):
    return milwaukee_team.pop(index)

@app.route("/add_athlete/<name>", methods = ["GET", "POST"])
def add_athlete(name):
    milwaukee_team.append(name)
    return milwaukee_team
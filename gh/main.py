"""
A GitHub info website

Author:
@FirestarDev (jdl-joseph on GitHub)

Usage:
For user info: /user_query?user={username}
For organization info: /org_query?org={organization}

Don't get lost! :3
"""

from flask import Flask, request, render_template
from pages import writeUserPage
from github import gh

app = Flask("app")
gh = gh()


@app.route("/")
def main():
  return render_template("home.html")

@app.route("/credits")
def credits():
  return render_template("credits.html")

@app.route("/user_query", methods=["GET"])
def uquery():
  user = request.args.get("user")
  
  if gh.isInvalid(user):
    return render_template("notfound.html")

  writeUserPage(user)
  return render_template("upage.html")

@app.route("/org_query", methods=["GET"])
def oquery():
  return "coming soon"

@app.route("/lost", methods = ["GET"]) 
def lost():
  # disable adblocker for this to work
  return "<iframe src='https://www.youtube.com/embed/Ik_ZPUbnEJs?ecver=1&autoplay=1' width='0' height='0' frameborder='0' allow='autoplay' allowfullscreen></iframe>"

app.run(host="0.0.0.0", port=8080, debug = True)
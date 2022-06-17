import pybase64
import requests
import json
from github import Github
from pprint import pprint



# 1. GitHub username
username = "cgbosse"
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
# pprint(user_data)

# Storing the data in a json file
user_data_json = user_data

with open('github_data.json', 'w') as f:
    json.dump(user_data_json, f)


# 2. Getting Public Repositories of a User

def get_repositories():
    # Code adapted from https://www.thepythoncode.com/article/using-github-api-in-python
    # Github username
    username = "cgbosse"
    # pygithub object
    g = Github()
    # get that user by username
    user = g.get_user(username)

    # Load the JSON File to then append the information
    data_file = open("github_data.json", "r")
    data = json.load(data_file)
    data["repo_names"] = []

    for repo in user.get_repos():
        print(repo)
        data["repo_names"].append(str(repo))
    # Writes the whole object with the appended information to the JSON File

    with open("github_data.json", "w") as data_file:
        data_file.write(json.dumps(data))


get_repositories()

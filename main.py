import requests
import json
from pprint import pprint

# GitHub username
username = "cgbosse"
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
pprint(user_data)

# Storing the data in a json file
user_data_json = user_data

with open('github_data.json', 'w') as f:
    json.dump(user_data_json, f)

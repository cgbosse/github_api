import requests
import json
import os
from github import Github
from github_token import GITHUB_TOKEN, user

# 1. GitHub username
username = user
print(username)

'''
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
'''

def get_user_basic(login_name:str):
    """Function which prints all the user's basic information including the list of the repositories
    login_name:
        string of the GitHub login name

    :return:
        a json contents that is printed to the 'github_data.json'
    """
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

def get_repositories(name: str):
    """
    Parameters
    ----------
    name: string

    """
    # Code adapted from https://www.thepythoncode.com/article/using-github-api-in-python
    # Github username

    # pygithub object
    g = Github()
    # get that user by username
    user_object = g.get_user(name)

    # Load the JSON File to then append the information
    data_file = open("github_data.json", "r")
    data = json.load(data_file)
    data["repo_names"] = []

    for repo in user_object.get_repos():
        print(repo)
        data["repo_names"].append(str(repo))
    # Writes the whole object with the appended information to the JSON File

    print(data)

    with open("github_data.json", "w") as data_file:
        data_file.write(json.dumps(data))


def get_org_repos_issues(org_name: str, separator: str, token: str) -> str:
    """Create a txt file with all the issues from an organization.

    Parameters
    ----------
    org_name : string 
        in small letters of the repository name
    separator : string 
        symbol for separating the columns
    token: string
        with the GitHub token

    Returns
    ------
    gen_list_issues.txt : txt 
        file with lines of the organization's issues' information
    """

    g = Github(token)
    print(token)

    # Get repositories for an organization
    org = g.get_organization(org_name)
    repos = org.get_repos()
    repos_id_list = []

    # Repo ID list printing
    print(repos_id_list)

    for repo in repos:
        print(repo)
        repos_id_list.append(repo.id)

        # Get issues for a repo
        issues = repo.get_issues()
        lines = []
        for issue in issues:
            print('----------------------------------')
            print(issue)

            issue_string = repo.name + separator + str(
                issue.state) + separator + str(issue.number) + separator + str(issue.title) + separator + str(
                issue.created_at) + separator + str(issue.user.login) + separator + str(issue.comments.real) + separator
            # print(issue_string)

            # issues_number_list.append(issue.number)

            # Getting the last comment if there are any comments
            if issue.comments.real > 0:

                comments = issue.get_comments()
                last_comment = comments[issue.comments.real - 1]
                # print(last_comment.updated_at)
                issue_string = issue_string + str(last_comment.updated_at) + separator
                # print(issue_string)
            else:
                issue_string = issue_string + "NA" + separator
                print(issue_string)

            # print(dir(issue))

            # Get labels on a particular issue
            labels = issue.get_labels()
            labels_number_list = []
            label_string = ""

            for label in labels:
                labels_number_list.append(label)
                # print(label)

                # Adding labels to the string
                label_string = label_string + "/" + str(label.name)
                # print(label_string)

            print(labels_number_list)

            issue_string = issue_string + label_string
            print(issue_string)
            lines.append(issue_string)

        with open('gen_list_issues.txt', 'a') as f:
            for line in lines:
                f.write(line)
                f.write('\n')


def get_repo_issues(repo_name: str):
    """Create a text file with

    :param
        repo_name: string

    :return:
        string lines of code dumped into the gen_list_issues.txt file
    """

    # Variables
    g = Github(username, GITHUB_TOKEN)
    separator = ";"

    user_object = g.get_user()
    #repo_name = "github_api"
    lines = []

    print(GITHUB_TOKEN)

    # Get repositories for an organization
    repo = user_object.get_repo(repo_name)

    # Get issues for a repo
    issues = repo.get_issues()

    for issue in issues:
        print('----------------------------------')
        print(issue)

        issue_string = repo_name + separator + str(issue.number) + separator + str(issue.title) + separator + str(issue.created_at) + separator + str(issue.user.name) + separator + str(issue.comments.real) + separator
        # print(issue_string)

        # issues_number_list.append(issue.number)

        # Getting the last comment if there are any comments
        if issue.comments.real > 0:

            comments = issue.get_comments()
            last_comment = comments[issue.comments.real - 1]
            # print(last_comment.updated_at)
            issue_string = issue_string + str(last_comment.updated_at) + separator
            # print(issue_string)
        else:
            issue_string = issue_string + "NA" + separator
            print(issue_string)

        # print(dir(issue))

        # Get labels on a particular issue
        labels = issue.get_labels()
        labels_number_list = []
        label_string = ""

        for label in labels:
            labels_number_list.append(label)
            #print(label)

            # Adding labels to the string
            label_string = label_string + "/" + str(label.name)
            # print(label_string)

        print(labels_number_list)

        issue_string = issue_string + label_string
        print(issue_string)
        lines.append(issue_string)

    with open('gen_list_issues.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write('\n')


'''
Execution of code
----------------------------
Examples of function uses:

- Getting all the user information of basic interest:
    get_user_basic(username)
    get_user_basic('cgbosse')


- Getting organization information:
    get_org_repos_issues("torrust", ";", GITHUB_TOKEN)
    get_org_repos_issues("nautilus-cyberneering", ";", GITHUB_TOKEN)

- Getting individual user's repositories:
    get_repositories(user)

- Getting individual user's repositories's issues:
    get_repo_issues()
    get_repo_issues("github_api")

'''

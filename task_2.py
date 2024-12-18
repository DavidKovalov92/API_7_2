import requests
from typing import List, Dict
from pprint import pprint


def get_recent_commits(repo_name: str) -> List[Dict[str, str]]:
    repo_name = repo_name.replace('/', ' ')
    OWNER, REPO = repo_name.split()
    params = {
        'per_page': 5,
        'page': 1,
    }


    req_ = requests.get(f'https://api.github.com/repos/{OWNER}/{REPO}/commits', params=params)
    if req_.status_code != 200:
        raise PermissionError(f'Status code {req_.status_code}')

    MY_JSON = req_.json()

    if MY_JSON:
        print('JSON is not empty')
    else:
        print('JSON is empty')

    commit_info = []


    for commit in MY_JSON:
        commit_info.append({
            "message": commit["commit"]["message"],
            "url": commit["html_url"],
            "author": commit["commit"]["author"]["name"],
            "date": commit["commit"]["author"]["date"]
        })

    return commit_info



pprint(get_recent_commits("octocat/Hello-World"))
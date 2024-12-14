from typing import List, Dict
import requests
from pprint import pprint

important_info = {
        'name': '',
        'description': '',
        'owner': '',
        'license': '',
        'created_at': '',
    }

def get_repository_info(repo_name: str) -> Dict[str, str]:
    repo_name = repo_name.replace('/', ' ')
    OWNER, REPO = repo_name.split()

    req_ = requests.get(f'https://api.github.com/repos/{OWNER}/{REPO}')

    MY_JSON = req_.json()

    clear_info = []
    for key in important_info.keys():
        if key in MY_JSON:
            clear_info.append(MY_JSON[key])

    return clear_info

pprint(get_repository_info("octocat/Hello-World"))
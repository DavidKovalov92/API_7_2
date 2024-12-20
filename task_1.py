from typing import Dict
import requests
from pprint import pprint

important_info = {
    'name': '',
    'description': '',
    'owner': '',
    'license': '',
    'created_at': '',
}

def status_(request):
    return request.status_code


def get_repository_info(repo_name: str) -> Dict[str, str]:
    repo_name = repo_name.replace('/', ' ')
    OWNER, REPO = repo_name.split()

    req_ = requests.get(f'https://api.github.com/repos/{OWNER}/{REPO}')

    if status_(req_) != 200:
        raise PermissionError(f"Status code: {status_(req_)}")


    MY_JSON = req_.json()


    if MY_JSON:
        print('JSON not empty')
    else:
        print('JSON is empty')
        return None



    clear_info = {}
    for key in important_info.keys():
        if key in MY_JSON:
            clear_info[key] = MY_JSON[key]

    return clear_info

pprint(get_repository_info("octocat/Hello-World"))
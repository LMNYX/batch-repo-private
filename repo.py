import requests, math, json

GITHUB_USERNAME = ""
GITHUB_TOKEN = ""

print("Getting amount of public repos... ", end="")

_X = requests.get(f"https://api.github.com/users/{GITHUB_USERNAME}", auth=(GITHUB_USERNAME, GITHUB_TOKEN)).json()
PublicRepos = _X['public_repos']
print(f"{PublicRepos}")
if(PublicRepos < 1):
    print("Nothing to private.")
    exit(0)

Pages = math.ceil(PublicRepos/100)

Repositories = []
CurrentPage = 1
print("Storing in the temporary array... ", end="")
while CurrentPage < Pages+1:
    _X = requests.get(f"https://api.github.com/users/{GITHUB_USERNAME}/repos?type=public&per_page=100&page={CurrentPage}", auth=(GITHUB_USERNAME, GITHUB_TOKEN)).json()
    for repo in _X:
        Repositories.append(repo['name'])
    CurrentPage += 1

print(f"{len(Repositories)}")
print("Privating... ", end="")

for repo in Repositories:
    _x = requests.patch(f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo}", data=json.dumps({ "private": True }), auth=(GITHUB_USERNAME, GITHUB_TOKEN))

print("OK")
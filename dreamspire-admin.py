import os
import requests
from git import Repo

# Config
local_repo_path = "/storage/emulated/0/DreamspireAdmin"
github_username = "YourGithubUsername"
repo_name = "dreamspire-admin"
token = "token = "ghp_yourNewTokenHere""

# Create new GitHub repo
headers = {"Authorization": f"token {token}"}
data = {"name": repo_name, "private": False}
res = requests.post("https://api.github.com/user/repos", headers=headers, json=data)

if res.status_code == 201:
    print(f"Repo '{repo_name}' created.")
else:
    print(f"Repo creation failed: {res.json()}")

# Set up local repo
if not os.path.exists(os.path.join(local_repo_path, ".git")):
    Repo.init(local_repo_path)

repo = Repo(local_repo_path)
origin = None

try:
    origin = repo.create_remote('origin', f"https://{github_username}:{token}@github.com/{github_username}/{repo_name}.git")
except:
    origin = repo.remote('origin')

repo.git.add(all=True)
repo.index.commit("Initial commit from Pydroid")
origin.push(refspec='master:main')
print("Code pushed to GitHub.")
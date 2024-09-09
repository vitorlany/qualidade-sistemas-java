import subprocess

CLONED_REPOS_PATH = "./repos"

def clone_repos(popular_repos):
    for repo in popular_repos:
        name = repo["node"]["name"]
        url = repo["node"]["url"]
        repo_path =  CLONED_REPOS_PATH + "/" + name

        print(repo_path)

        subprocess.run(["git", "clone", url, repo_path])

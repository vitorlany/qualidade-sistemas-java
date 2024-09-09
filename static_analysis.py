import subprocess

CLONED_REPOS_PATH = "./repos"
CK_ANALYSIS_PATH = "./ck_results"
CK_PATH = "../ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"

def get_metrics(popular_repos):
    clone_repos(popular_repos)
    run_ck(popular_repos)

# Clonar repos para pasta ./repos
def clone_repos(popular_repos):
    for repo in popular_repos:
        name = repo["node"]["name"]
        url = repo["node"]["url"]
        repo_path =  CLONED_REPOS_PATH + "/" + name

        print(repo_path)

        subprocess.run(["git", "clone", url, repo_path])

# Executar análise estática
def run_ck(popular_repos):
    subprocess.run(["mkdir", CK_ANALYSIS_PATH])

    for repo in popular_repos:
        name = repo["node"]["name"]
        repo_path =  CLONED_REPOS_PATH + "/" + name
        results_path =  CK_ANALYSIS_PATH + "/" + name + "/"

        print(results_path)

        subprocess.run(["mkdir", results_path])
        subprocess.run(["java", "-jar", CK_PATH, repo_path, "true", "0", "false", results_path])

import subprocess
import threading

CLONED_REPOS_PATH = "./repos"
CK_ANALYSIS_PATH = "./ck_results"
CK_PATH = "../ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"

def get_metrics(popular_repos):
    subprocess.run(["mkdir", CLONED_REPOS_PATH])
    subprocess.run(["mkdir", CK_ANALYSIS_PATH])
    divided_by = 10
    part = len(popular_repos) // divided_by

    def threaded_process(start, end):
        process_in_range(popular_repos, start, end)

    threads = []
    for i in range(0, divided_by):
        start = i * part
        end = (i + 1) * part        
        thread = threading.Thread(target=threaded_process, args=(start, end))
        threads.append(thread)
        thread.start()     

    for thread in threads:
        thread.join()

def process_in_range(popular_repos, start, end):
    for i in range(start, end):
        repo = popular_repos[i]
        repo_name = repo["node"]["name"]
        clone_repos(repo_name, repo["node"]["url"])
        run_ck(repo_name)
        delete_clone(repo_name)

# Clonar repos para pasta ./repos
def clone_repos(name, url):
    repo_path =  CLONED_REPOS_PATH + "/" + name


    subprocess.run(["git", "clone", url, repo_path])

def delete_clone(name):
    repo_path =  CLONED_REPOS_PATH + "/" + name

    subprocess.run(["rm", "-rf", repo_path])

# Executar análise estática
def run_ck(repo_name):
    subprocess.run(["mkdir", CK_ANALYSIS_PATH])

    repo_path =  CLONED_REPOS_PATH + "/" + repo_name
    results_path =  CK_ANALYSIS_PATH + "/" + repo_name + "/"

    # print(results_path)

    subprocess.run(["mkdir", results_path])
    subprocess.run(["java", "-jar", CK_PATH, repo_path, "true", "0", "true", results_path])

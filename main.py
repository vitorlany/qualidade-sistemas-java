from get_data import get_popular_java_repos

if __name__ == "__main__":
    num_repos = 1000
    try:
        popular_repos = get_popular_java_repos(num_repos)
        print(popular_repos)
    except Exception as e:
        print(e)
    exit(0)

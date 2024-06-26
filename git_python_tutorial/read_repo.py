import os
from git import Repo

COMMITS_TO_PRINT = 5
DEFAULT_REPO_PATH = '/tmp/python_sanbox'

def print_commit(commit): # print commit details
    print('------------')
    print(str(commit.hexsha)) # 40-character SHA-1 hash for the commit
    print("\"{}\" by {} ({})".format(
        commit.summary,
        commit.author.name,
        commit.author.email
    ))

    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(
        commit.count(),
        commit.size
    )))


def print_repository(repo): # print repo details
    print("Repo description: {}".format(repo.description))
    print("Repo active branch is {}".format(repo.active_branch))
    for remote in repo.remotes:
        print("Remote named '{}' with URL '{}'".format(remote, remote.url))
    print('Last commit for Repo is {}.'.format(str(repo.head.commit.hexsha)))


if __name__=='__main__':
    repo_path = os.getenv('GIT_REPO_PATH', DEFAULT_REPO_PATH)
    repo = Repo(repo_path) # Repo object used to programmatically interact with Git repositories 
    # Check the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits('main'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
    else:
        print('Could not load repository at {}.'.format(repo_path))

import os
from git import Repo

COMMITS_TO_PRINT = 5

def print_commit(commit):
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
        commit.size()
    )))


if __name__=='__main__':
    pass

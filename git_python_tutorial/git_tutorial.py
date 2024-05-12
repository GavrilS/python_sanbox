import os
from git import Repo, Remote


DEFAULT_REPO_PATH = '/tmp/python_sanbox'


def get_heads(repo):
    heads = repo.heads
    active_head = repo.head
    print('----------------------------\nHeads')
    print(heads)
    # for head in heads:
    #     print('Head: ', end=' ')
    #     print(head)
    print(f'----------------------\nActive head: {active_head} with reference: {active_head.reference}')
    # print(active_head)
    return active_head


def get_head_commit(head):
    print(head.commit)

def get_remote_info(remote):
    print('--------------------')
    print('Fetching remote info')
    fetch_info = remote.fetch()
    print(type(fetch_info))
    print(fetch_info)


if __name__=='__main__':
    repo_path = os.getenv('GIT_REPO_PATH', DEFAULT_REPO_PATH)
    repo = Repo(repo_path) # Repo object used to programmatically interact with Git repositories 
    # Check the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        head = get_heads(repo)
        get_head_commit(head)
        remote = Remote(repo, str(head))
        print('Remote: ', remote)
        get_remote_info(remote)
    else:
        print('Could not load repository at {}.'.format(repo_path))

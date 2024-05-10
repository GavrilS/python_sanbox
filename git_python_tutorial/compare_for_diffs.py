import os
from git import Repo, Remote


DEFAULT_REPO_PATH = '/tmp/python_sanbox'

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
        remote = Remote(repo, 'main')
        print('Remote: ', remote)
        get_remote_info(remote)
    else:
        print('Could not load repository at {}.'.format(repo_path))

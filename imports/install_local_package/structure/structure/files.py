

def unique_path(directory):
    '''Find a path that does not exist.'''
    counter = 0
    while True:
        counter += 1
        path = directory / f"UPDATED_STRUCTURE/{counter}"
        if not path.exists():
            return path


def add_empty_file(path):
    '''Create an empty file at the given path.'''
    print(f"Creating file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()

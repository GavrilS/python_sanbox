"""
Test command: 
python3 imports/install_local_package/structure/structure/structure.py ./imports/install_local_package/structure/structure/
"""
import pathlib
import sys

# Works when ran directly with the above command, but does not work when ran from a script from outside the package
import files
# Works when ran from a script from outside the package, but does not work when run directly with above command
# from . import files


def main():
    # Read path from the command line
    try:
        root = pathlib.Path(sys.argv[1]).resolve()
        print('Initial root: ', root)
        print('type(root): ', type(root))
    except IndexError:
        print('Need at least one argument: the root of the original file tree')
        raise SystemExit()
    
    # Re-creating the file structure
    new_root = files.unique_path(pathlib.Path.cwd())
    print('New root: ', new_root)
    print('type(new_root): ', type(new_root))
    for path in root.rglob('*'):
        print('Current path is: ', path)
        if path.is_file() and new_root not in path.parents:
            relative_path = path.relative_to(root)
            print('relative_path: ', relative_path)
            files.add_empty_file(new_root / relative_path)


if __name__=='__main__':
    main()            

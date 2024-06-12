from pathlib import Path
import importlib


def test_path():
    file = Path(__file__).stem
    full_path = Path(__file__)
    print(file)
    print(full_path)

    for dir in str(full_path).split('/'):
        print('Dir: ', dir)

    get_relative_path = Path(__file__).parent.resolve()
    print(get_relative_path)
    print(type(get_relative_path))


def get_import_path(revert_levels):
    full_path = str(Path(__file__).parent.resolve()).split('/')
    print('Full path: ', full_path)
    new_path_array = full_path[:-revert_levels]
    new_path = ''
    for dir in new_path_array:
        new_path += dir + '/'
    
    print('New path: ', new_path)
    # print('New path: ', Path(new_path))

    return new_path


def add_import_module(project_path, module_path):
    import_path = project_path + module_path
    print('Import path: ', import_path)
    if import_path.startswith('/'):
        import_path = import_path[1:]
    mod = importlib.import_module(import_path.replace('/', '.'))
    return mod


def test_printer(mod):
    mod.print_greeting()
    mod.print_message('This is a test!')


def load_module_by_full_path(module_path):
    module_name = 'custom_printer'

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    custom_printer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(custom_printer)

    custom_printer.print_greeting()


if __name__=='__main__':
    # test_path()
    # project_path = get_import_path(1)
    # mod = add_import_module(project_path, 'modules/printer')

    # test_printer(mod)
    load_module_by_full_path('/mnt/c/Users/Gari/git/python_sanbox/imports/relative_imports/modules/printer.py')

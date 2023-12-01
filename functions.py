import os,sys
FILEPATH = "todos.txt"


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_todos(filepath=FILEPATH):
    """Reads a text file and return the list of the to-do items."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(values, filepath=FILEPATH):
    """Writing the to-do items list in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(values)





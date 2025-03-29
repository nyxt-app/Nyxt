from .create_app import __init__ as createApp
from .create_component import __init__ as createComponent
from .get_children import __init__ as getChildren
from .start import __init__ as Start
from .router import Router

def loadFile(path):
    """
    The function `loadFile` reads and returns the contents of a file specified by the given path.
    
    :param path: The `path` parameter in the `loadFile` function is a string that represents the file path of the file you want to load and read. It should be the location of the file on your system that you want to open and read
    
    :return: The function `loadFile` reads the contents of a file located at the specified `path` and returns the content of the file as a string.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()
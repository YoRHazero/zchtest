"""
FileBox class
A class to represent a file box.
This module provides a class to represent a file box with a name and path.
"""

class FileBox:
    """
    A class to represent a file box.
    
    Example
    -------
    >>> box = FileBox("example", "/path/to/example")
    >>> box.give_box_path()
    '/path/to/example'
    >>> box.name
    'example'
    >>> box.path
    '/path/to/example'
    >>> box.give_box_path()
    '/path/to/example'
    """

    def __init__(self, name: str, path: str):
        """
        Initialize the FileBox with a name and path.

        Parameters
        ----------
        name : str
        The name of the file box.
        
        path : str
        Get the path of the file box.
        
        Example
        -------
        >>> box = FileBox("example", "/path/to/example")
        """
        self.name = name
        self.path = path

    def give_box_path(self) -> str:
        """
        Get the path of the file box.

        Returns
        -------
        str
            The path of the file box.
        
        Example
        -------
        >>> box = FileBox("example", "/path/to/example")
        >>> box.give_box_path()
        '/path/to/example'
        """
        return self.path
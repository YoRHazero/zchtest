"""
zchtest.manager
A module for managing file boxes in the zchtest package.
This module provides a function to get the base name of a file box.
"""
import os
from .box import FileBox

def get_box_basename(box: FileBox) -> str:
    """
    Get the base name of the file box.

    Parameters
    ----------
    box : FileBox
        The file box to get the base name from.

    Returns
    -------
    str
        The base name of the file box.

    Example
    -------
    >>> box = FileBox("example", "/path/to/example")
    >>> get_box_basename(box)
    'example'
    """
    return os.path.basename(box.give_box_path())
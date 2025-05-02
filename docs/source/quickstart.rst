Quickstart Guide
================

This quickstart will show you how to install and use the basic features of the zchtest package.

Installation
------------

First, install from PyPI:

.. code-block:: bash

   pip install zchtest
   # — or for editable install during development —
   pip install -e .

Basic Usage
-----------

Import the main classes and functions:

.. code-block:: python

   from zchtest.box import FileBox
   from zchtest.manager import get_box_basename

Create a FileBox and get its path:

.. code-block:: python

   box = FileBox("example", "/path/to/example")
   print(box.give_box_path())
   # 输出: /path/to/example

Use a helper function:

.. code-block:: python

   basename = get_box_basename("/path/to/example/file.txt")
   print(basename)
   # 输出: file.txt

Further Reading
---------------

- :ref:`API <genindex>` for full list of modules and functions.
Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section enlists prerequisites required by the napari plugins.


Python
-----------------------------------------

All napari plugins are written in Python which requires a Python interpreter for execution. We recommend to install Python from one of the following sources...

+----------------------------+------------------------------------------------+---------------------------------------------------------------------+
| Provider                   | URL                                            | Description                                                         |
+============================+================================================+=====================================================================+
| Python Software Foundation | https://www.python.org/downloads/              | Python interpreter (no additional packages)                         |
+----------------------------+------------------------------------------------+---------------------------------------------------------------------+
| Anaconda Inc.              | https://docs.conda.io/en/latest/miniconda.html | Python interpreter + conda package manager (no additional packages) |
+----------------------------+------------------------------------------------+---------------------------------------------------------------------+
| Anaconda Inc.              | https://docs.anaconda.com/anaconda/install/    | Python interpreter + conda package manager + 100+ packages          |
+----------------------------+------------------------------------------------+---------------------------------------------------------------------+

While the Python Software Foundation provides a lightweight installer without any packages Anaconda Inc. provides a distribution with over 100 packages which, in return, needs more than 3Gb of disk space.

    Note: To avoid conflicts between napari plugins and other Python packages, it is recommended to create/use a new virtual environment. Please refer to "`The Python Tutorial <https://docs.python.org/3/tutorial/venv.html>`_" for further information.


Git
-----------------------------------------

By now, all napari plugins are available via private GitHub repositories. Hence, a git client is required for authentication and downloading/installing Python packages. The git command line interface (CLI) client can be downloaded from https://git-scm.com/download/. However, if you prefer a graphical user interface (GUI) you can find a full list of available GUI clients `here <https://git-scm.com/downloads/guis>`_.

If you are new to git please refer to the `official documentation <https://git-scm.com/doc>`_ and the `introduction videos <https://git-scm.com/videos>`_.

    Note: The documentation assumes as you installed the CLI client and as you use a terminal to execute the git commands. This way, we can keep the documentation tidy as each GUI client is different in its behaviour and has a different feature set. Please refer to your GUI client's docunmentation on how to perform individual git commands via the graphical user interface.


Napari
-----------------------------------------

`Napari <https://napari.org/>`_ is a fast, interactive, multi-dimensional image viewer for Python.

Minimal requirements

.. tabularcolumns:: |\Y{0.5}|\Y{0.5}|

+----------------------------+----------------------------------------------------------------------------------------------------+
| Operating System           | Python                                                                                             |
+============================+====================================================================================================+
| Windows, Linux, MacOS      | v3.7 and later                                                                                     |
+----------------------------+----------------------------------------------------------------------------------------------------+

Napari can be installed via pip:

.. code:: python

    pip install napari[all]

.. 

    Note: napari[all] includes the PyQt5 GUI backend which is required for the graphical user interface. 


A full installation instruction is available via https://napari.org/. 

=========================================
Napari Plugins
=========================================

.. only:: html

   .. contents:: Table of Contents


About
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This documentation is designed for end-users of the Fractal Analytics Platform's napari plugins. Topics for developers and system administrations are covered in separate documents.


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


Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All napari plugins are available via https://github.com/fractal-napari-plugins-collection.

Minimal requirements:

.. tabularcolumns:: |\Y{0.5}|\Y{0.5}|

+----------------------------+----------------------------------------------------------------------------------------------------+
| Operating System           | Python                                                                                             |
+============================+====================================================================================================+
| Windows, Linux, MacOS      | v3.7 and later                                                                                     |
+----------------------------+----------------------------------------------------------------------------------------------------+

The plugins can be installed via pip...

.. code:: shell

    pip install git+https://github.com/fractal-napari-plugins-collection/<napari-plugin>.git

... or by using git manually:

.. code:: shell

    git clone https://github.com/fractal-napari-plugins-collection/<napari-plugin>
    cd <napari-plugin>
    pip install .


Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following section contains usage instructions for the Napari plugins. For more details on how to use Napari itself please refer to the `Napari tutorials <https://napari.org/tutorials/index.html>`_.

    Note: Please verify as all plugins were installed correctly. You should find them in Napari's "Plugins/List Installed Plugins..." menu.


PTIF Reader
-----------------------------------------

    Note: Reading fractions of an image (a.k.a. lazy loading) requires advanced data structures which Napari only supports recently. For a smooth user-experience it is recommended to activate the NAPARI_OCTREE flag **before** running Napari. You can do so from the command line **before** running napari.

    +----------------------------+----------------------------------------------------------------------------------------------------+
    | Windows                    | Linux/Mac                                                                                          |
    +============================+====================================================================================================+
    | .. code:: batch            | .. code:: shell                                                                                    |
    |                            |                                                                                                    |
    |    SET NAPARI_OCTREE=1     |    export NAPARI_OCTREE=1                                                                          |
    |    napari                  |    napari                                                                                          |
    |    SET NAPARI_OCTREE=0     |    export NAPARI_OCTREE=0                                                                          |
    +----------------------------+----------------------------------------------------------------------------------------------------+

    We recommend to create a batch/shell script with the above commands. Deactivating the octree feature at the end avoids conflicts when using Napari with non-multi-scale images later on.
    If you are not familiar with batch/shell scripts please refer to the following tutorials for `Windows <https://www.tutorialspoint.com/batch_script/batch_script_files.htm>`_ and `Linux/Mac <https://www.tutorialspoint.com/unix/shell_scripting.htm>`_.

Given you have a multi-scale (pyramidal) TIF file with a PTIF extension, you can simple drag-n-drop the image into Napari or open the file from within Napari via the "File/Open File(s)..." menu.

    Note: Fractal does not yet provide a tool to convert large-scale images into multi-scale images. For testing purposes, we recommend to install `ImageMagick <https://imagemagick.org/index.php>`_ and convert e.g. the test001.tif image into a test001.ptif image using the following command:

    .. code:: shell

       convert.exe test001.tif -define tiff:tile-geometry=1024x1024 -compress jpeg ptif:test001.ptif

    Please note as ImageMagick is a very powerful tool which allows you to specify many more options via the command line. For more details please refer to the `official reference <https://imagemagick.org/script/command-line-processing.php>`_.


XML Reader
-----------------------------------------

The XML file format is an intermediate solution for reading a series of images. The reader expects a valid XML file structure with a list of "image" elements. Following a simple example:

.. code:: xml

   <?xml version="1.0" ?>
   <images>
       <image file=".\test001.tif"/>
       <image file=".\test002.tif"/>
       <image file=".\test003.tif"/>
   </images>

Please note as all images must have the same dimensions. For more information/updates please refer to the following `GitHub Issue <https://github.com/napari/napari/issues/661>`_.

Given you have a conform XML file, you can simple drag-n-drop the file into Napari or open the file from within Napari via the "File/Open File(s)..." menu.


ROI Reader
-----------------------------------------

The ImageJ/FIJI ROI file format is an intermediate solution for reading shape information. You can create ROIs via ImageJ's/FIJI's `ROI manager <https://imagej.nih.gov/ij/docs/guide/146-30.html#sub:ROI-Manager...>`_. By selecting/exporting multiple ROIs ImageJ/FIJI creates a ZIP archive which contains all selected ROIs as individual files.

    Note: The ROI reader plugin currently support the following ROI types: polygon, rect, oval, line, freeline and freehand.

Given a ROI file or ZIP file contianing multiple ROIs, you can simple drag-n-drop the file into Napari or open the file from within Napari via the "File/Open File(s)..." menu.


Error Handling
-----------------------------------------
TBD

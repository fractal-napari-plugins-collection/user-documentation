#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode'
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Fractal Analytics Platform'
copyright = (
    u'(c) 2020 Friedrich Miescher Institute for Biomedical Research | University of Zurich'
)
author = u'Dario Vischi'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# These patterns also affect html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, generates auto-summary automatically.
autosummary_generate = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'nature'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Customize the HTML context
html_context = {
    'css_files': [
        '_static/style.css',  # override wide tables in RTD theme
    ],
 }

# Customize the HTML side menu
html_sidebars = {
    '**': [
        'globaltoc.html',
        #'relations.html',
        'sourcelink.html',
        'searchbox.html'
    ]
}


# -- Options for LaTeX output ---------------------------------------------

latex_title = u'Fractal Analytics Platform \\\\Napari Plugins'
latex_header = u'Fractal Analytics Platform | Napari Plugins'
latex_authors = u'Friedrich Miescher Institute for Biomedical Research \\and University of Zurich'


latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble' : r"""
    """,
    'extraclassoptions': 'openany',  # https://github.com/sphinx-doc/sphinx/issues/2622
    'maketitle': r"""
    \noindent\rule{\textwidth}{1pt}\par
        \begingroup %% for PDF information dictionary
            \def\endgraf{ }\def\and{\& }
            \pdfstringdefDisableCommands{\def\\{, }} %% overwrite hyperref setup
            \hypersetup{
                pdfauthor={%s},
                pdftitle={%s}
            }
        \endgroup
    \begin{flushright}
        %% \sphinxlogo
        \sffamily\bfseries  %% \py@HeaderFamily
        \vspace{75pt}
        {\Huge %s }\par
        \vspace{25pt}
        {\itshape\large Release %s \releaseinfo}\par
        \vspace{150pt}
        {\Large
            \begin{tabular}[t]{c}
                %s
            \end{tabular}}\par
        \vspace{25pt}
        \today \par
    \end{flushright}
    \setcounter{footnote}{0}
    \let\thanks\relax\let\maketitle\relax
    """ % (
        latex_authors,
        latex_header,
        latex_title,
        release,
        latex_authors
    )
}

latex_documents = [
    (
        master_doc,
        'fap_napari_plugins.tex',
        u'Fractal Analytics Platform | Napari Plugins',
        latex_authors,
        'manual',
        True  # toctree_only
    ),
]

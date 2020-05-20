import os
import sys
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('.'))

# Include todo list
todo_include_todos = True

# -- Project information -----------------------------------------------------

project = 'sphinxcontrib-pylit'
copyright = '2020, Roie R. Black'
author = 'Roie R. Black'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

master_doc = 'contents'
extensions = [
        'sphinx.ext.todo',
        'sphinx_ext.wordcount',
        'sphinxcontrib.bibtex',
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_examples']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

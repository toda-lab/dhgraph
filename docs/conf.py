# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

from dhgraph import __version__ as dhgraph_version

project = 'dhgraph'
copyright = '2024, Takahisa Toda'
author = 'Takahisa Toda'
version = dhgraph_version
release = dhgraph_version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "pallets_sphinx_themes",
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_removed_in",
    "sphinxcontrib_trio",
]

templates_path = ['_templates']

source_suffix = ".rst"

pygments_style = "sphinx"

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

sys.path.append(os.path.abspath("_themes"))
html_theme_path = ["_themes"]
html_theme = "flask"

html_static_path = ['_static']

todo_include_todos = True

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# pylint: disable=C0103,C0114,W0622

# Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
from source.myp_mocks import setup_micropython_mocks

sys.path.insert(0, os.path.abspath("."))  # Add source directory to path
sys.path.insert(0, os.path.abspath(os.path.join("..", "sbc-sdk", "src")))
sys.path.append(os.path.abspath(os.path.join("..", "sbc-sdk", "tests", "__mocks__")))

# Setup MicroPython mocks
setup_micropython_mocks()

autodoc_preserve_defaults = True
autodoc_mock_imports = [
  "utime",
  "machine",
  "micropython",
  "gc",
  "network",
  "socket",
  "ssl",
  "ubinascii",
  "uhashlib",
  "ujson",
  "ure",
  "uselect",
  "ustruct"
]

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sbc-docs'
copyright = '2025, EPS Works SL'
author = 'EPS Works SL'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "myst_parser",
  "sphinx.ext.autodoc",
  "sphinx.ext.napoleon",
  "sphinx_autodoc_typehints",
]

myst_enable_extensions = ["html_image", "colon_fence", "deflist"]

add_module_names = False

def skip_module_docstring(_app, what, _name, _obj, _options, lines):
    """Skip module docstrings."""
    if what == "module":
        lines.clear()  # removes the docstring contents

def setup(app):
    """Setup autodoc-process-docstring hook."""
    app.connect("autodoc-process-docstring", skip_module_docstring)


# Type hints
always_use_bars_union = True
typehints_fully_qualified = False
always_document_param_types = True
typehints_defaults = "comma"
typehints_use_signature = False
typehints_use_signature_return = True

# Napoleon config
napoleon_google_docstring = True
napoleon_include_init_with_doc = False
napoleon_use_admonition_for_examples = True
napoleon_include_private_with_doc = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_attr_annotations = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

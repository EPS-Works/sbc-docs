# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

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

add_module_names = False

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

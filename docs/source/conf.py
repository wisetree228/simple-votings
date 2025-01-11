import os
import sys

sys.path.insert(0, os.path.abspath('../../')) #Путь к проекту
os.environ['DJANGO_SETTINGS_MODULE'] = 'simple-votings-py-masters.settings'

import django
django.setup()


project = 'SVPM'
copyright = '2025, Alexey, Georgiy, Pavel, Egor, Matvey, Darya'
author = 'Alexey, Georgiy, Pavel, Egor, Matvey, Darya'
release = 'v0.7b'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

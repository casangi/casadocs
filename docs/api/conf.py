######################################
# API text file generation config
######################################

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx_automodapi.automodapi',
    'recommonmark'
]
todo_include_todos = True
add_module_names = False
numpy_show_class_members = False
autosummary_generate = False
autodoc_member_order = 'bysource'

#List of imports to mock (this ensures readthedocs works)
autodoc_mock_imports = ['numcodecs','os','numpy','time','xarray','numba','itertools','zarr']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'api'

language = None

exclude_patterns = ['build', 'tasks', 'tools', 'examples', 'notebooks', 'Thumbs.db', '.DS_Store']

#!/usr/bin/env python
#
# Sphinx configuration file
# see metadata.yaml in this repo to update document-specific metadata

import os

from documenteer.conf.technote import *

extensions.extend(['jupyter_sphinx'])
exclude_patterns = ['venv', '.ipynb_checkpoints', 'README.rst']

# Add intersphinx inventories as needed
# http://www.sphinx-doc.org/en/stable/ext/intersphinx.html
# Example:
#
#     intersphinx_mapping['python'] = ('https://docs.python.org/3', None)

ipy_config = get_config()


# Set old completion style
ipy_config.TerminalInteractiveShell.display_completions = 'readlinelike'

ipy_config.InteractiveShellApp.extensions = ['autoreload']

ipy_config.InteractiveShellApp.exec_lines = [
    'import re, sys, requests',
    '%autoreload 2'
    'print("Warning: disable autoreload in ipython_config.py to improve performance.")',
]

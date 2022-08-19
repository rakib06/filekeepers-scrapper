import os


def make_dir_if_not_exits():
    'skip' if os.path.exists(
        'local/screenshot/') else os.makedirs('local/screenshot/')
    'skip' if os.path.exists(
        'local/data/') else os.makedirs('local/data/')
    'skip' if os.path.exists(
        'local/logs/') else os.makedirs('local/logs/')

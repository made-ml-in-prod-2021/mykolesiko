"""
    some assistance utils
"""
import os

def get_path(path: str, file: str):
    """
        concat pathes
    """
    return os.path.join(path, file)

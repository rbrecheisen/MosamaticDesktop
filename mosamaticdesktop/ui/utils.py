import os
import sys


def resource_path(relative_path):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    return os.path.join(base_path, relative_path)


def is_macos():
    return sys.platform.startswith('darwin')
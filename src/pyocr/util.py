#!/usr/bin/env python

import os
import sys


def to_unicode(string):
    if hasattr(string, 'decode'):
        return string.decode('utf-8')
    return string


def is_on_path(exec_name):
    """
    Indicates if the command 'exec_name' appears to be installed.

    Returns:
        True --- if it is installed
        False --- if it isn't
    """
    if sys.platform == 'win32':
        #Tesseract keeps its own Environment Variable on Windows
        all_paths = os.environ["PATH"].split(os.pathsep)
        if os.environ.get('TESSDATA_PREFIX'):
            all_paths.append(os.environ.get('TESSDATA_PREFIX'))

        for dirpath in all_paths:
            path = os.path.join(dirpath, exec_name + '.exe')
            if os.path.exists(path) and os.access(path, os.X_OK):
                return True
    else:
        for dirpath in os.environ["PATH"].split(os.pathsep):
            path = os.path.join(dirpath, exec_name)
            if os.path.exists(path) and os.access(path, os.X_OK):
                return True

    return False

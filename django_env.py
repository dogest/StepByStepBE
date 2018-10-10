import os
import sys

import django


def setup_environment():
    pathname = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, pathname)
    sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StepByStep.settings")


setup_environment()
django.setup()

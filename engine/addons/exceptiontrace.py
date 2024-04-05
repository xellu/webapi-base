import sys

from dataforge import console

def handler(exc_type, exc_value, exc_traceback):
    console.error(f"{exc_type.__name__}: {exc_value}")

sys.excepthook = handler
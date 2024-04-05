import os
from dataforge import console

try:
    import engine
except Exception as err:
    console.error(err)
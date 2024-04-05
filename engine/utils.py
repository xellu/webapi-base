import json
import hashlib
import random, string  

from engine.core import Config

def hashstr(string):
    """
    :string: a string to hash\n\nHashes a string using sha256
    """
    return str(hashlib.sha256(string.encode()).hexdigest())

def randomstr(length: int):
    """
    :length: length of the string to generate\n\nGenerates a random string of letters
    """
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def params(string):
    for key, value in vars(Config).items():
        string = string.replace(f"%{key}%", str(value))
    return string
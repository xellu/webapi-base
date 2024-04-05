import json

import flask
import flask_limiter
from flask_limiter.util import get_remote_address
from flask import Flask, Blueprint

from dataforge import console
from engine.core import Config

# Blueprint Loader

class BlueprintLoader:
    def __init__(self, app: Flask):
        self.app = app
        self.bps = []

    def load(self):
        for bp in self.bps:
            self.app.register_blueprint(bp)
        Info(f"Loaded {len(self.bps)} route blueprints")
    
    def new(self, blueprint: flask.Blueprint):
        self.bps.append(blueprint)
    
# Responding & Payload validation

# -- Responding
def Reply(**kwargs) -> str:
    """
    Returns a JSON response\n\n
    Example: `Reply(hello="world")` -> `{"hello": "world"}`
    """
    return json.dumps(kwargs)

# -- Payload validation
def invalidate(payload, **args): #code from doorsmc webserver api
    """
:payload: a payload to check\n:args: keys to check the payload for\n\nChecks if a payload is valid
    """
    for key in args:
        if key not in payload:
            return True
    return False

def fetch_data(request):
    """
:request: a flask request object to fetch data from\n\nLoads data from a request
    """
    try:
        return json.loads(request.get_data())
    except:
        return {}
    
def Require(request, **args):
    """
:request: a flask request object to fetch data from\n
:args: keys to check the request payload for\n\n
Loads data from a request and checks if it is valid (returns None if invalid)\n
Example:
    request body = `{"hello": "world"}`\n
    `Require(request, hello=str)` -> `{"hello": "world"}`\n
    `Require(request, world=str)` -> `None`
    """
    data = fetch_data(request)
    if invalidate(data, **args):
        return None
    return data

#-----------------------
    
# Variables

Info = console.tag(console.COLOR.BLUE, "ROUTER").print
Warn = console.tag(console.COLOR.YELLOW, "ROUTER", console.Level.WARN).print
Error = console.tag(console.COLOR.RED, "ROUTER", console.Level.ERROR).print

App = Flask(Config.name)
Limiter = flask_limiter.Limiter(app=App, key_func=get_remote_address)

BPLoader = BlueprintLoader(App)


# Routers

v1example = Blueprint("Example", __name__, url_prefix="/api/v1/example")
BPLoader.new(v1example)
from engine.router import Reply, Require, v1example
from engine.core import Config

from flask import request

@v1example.route("/", methods=["POST"])
def example():
    data = Require(request, hello=str) #checks if the request payload has required keys and returns the data (if valid; None if invalid)
    
    if data is None: #Require returns None if the payload is invalid
        return Reply(error="Invalid payload"), 400 #returns a JSON response with a 400 status code
    
    if data["hello"] == "config":
        return Reply(setting=Config.more_settings) #returns a JSON response -> {"setting": (value of more_setting in config.json)}
    
    return Reply(message="Hello, World!")

#send a POST request to http://localhost/api/v1/example/ with a JSON payload of {"hello": "world"} to see the response
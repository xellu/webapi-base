import os

from dataforge import console

from engine.shell.core import Say
from engine.core import Autosave

def main():
    Say(f"Server shutdown initiated")
    
    Autosave.stop()
    Say("Service stopped: AutosaveManager")
    
    console.logging.save()
    console.logging.stop()
    Say("Service stopped: Logging")
    
    
    
    Say("Server stopped, exiting")
    
    os._exit(0)
    
    
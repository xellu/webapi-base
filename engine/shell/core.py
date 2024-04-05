import threading

from dataforge import console
from engine.core import Version, Config

Say = console.tag(console.COLOR.GREEN, "Shell").print

class ShellManager:
    def __init__(self):
        self.commands = []
    
    def register(self, command):
        self.commands.append(command)
        
    def run(self):
        Say(f"Running {Config.name} Shell (v{Version.Release})")
        
        threading.Thread(target=self.loop).start()
        
    def loop(self):
        while True:
            try:
                command = input("")
                data = self.parse(command)
                self.call(data)

            except (KeyboardInterrupt, SystemExit):
                console.warn("Use 'stop' to shutdown the service")
                pass

            except Exception as error:
                if str(error) == "": #ctrl+c - does not call keyboard interupt?
                    console.warn("Forced shutdown initiated, stopping service")
                    self.execute("stop", source="ShellManager")
                
                console.error(f"Shell error: {error}")
                
    def call(self, data):
        for cmd in self.commands:
            if cmd.command == data["command"]:
                out = cmd.func(*data["args"], **data["kwargs"])
                if out:
                    Say(f"{cmd.command} -> {out}")
                    return out
                
    def parse(self, text):
        #example format of the command:
        #command arg1 arg2 --arg3=value
        
        data = {
            "command": None,
            "args": [],
            "kwargs": {}
        }
        
        parts = text.split(" ")
        data["command"] = parts[0]
        
        for part in parts[1:]:
            if part.startswith("--"):
                key, value = part[2:].split("=")
                data["kwargs"][key] = value
            else:
                data["args"].append(part)
                
        return data
    
    def execute(self, command, source = "External Source"):
        console.warn(f"Running a command from an external source: {source}")
        
        data = self.parse(command)
        output = self.call(data)
        return output
    
Shell = ShellManager()
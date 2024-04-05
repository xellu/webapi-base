from dataforge import console
import logging

class LoggingManager:
    def __init__(self, tag, obj):
        self.tag = tag
        self.obj = obj
        
    def call(self, msg, *args, **kwargs):
        if self.obj.disabled: return
        if args: msg = msg % args

        self.tag.print(msg)

class LoggingPatch():
    def __init__(self, items):
        self.items = items

    def patch(self):
        for item in self.items:
            logger = item.logger
            logger.info = LoggingManager(console.tag(console.COLOR.BLUE, logger.name), item).call
            logger.warn = LoggingManager(console.tag(console.COLOR.YELLOW, logger.name, console.Level.WARN), item).call
            logger.warning = logger.warn
            logger.error = LoggingManager(console.tag(console.COLOR.RED, logger.name, console.Level.ERROR), item).call
            logger.fatal = LoggingManager(console.tag(console.COLOR.RED, logger.name, console.Level.FATAL), item).call
   

class Patch:
    def __init__(self, logger, disable=False):
        self.logger = logger
        self.disabled = disable

LoggingPatch([
    Patch(logging.getLogger("discord.client")),
    Patch(logging.getLogger("discord.gateway")),
    Patch(logging.getLogger("werkzeug"), disable=True)
    
]).patch()
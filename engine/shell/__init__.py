from engine.shell.core import Shell
from dataforge.database import Item

from .commands import (stop, help, about, db, attrfix)

Shell.register(Item(command="help", func=help.main, description="Shows this help message", args = [Item(name="command", require=False)]))
Shell.register(Item(command="about", func=about.main, description="Shows information about the server", args = []))
Shell.register(Item(command="stop", func=stop.main, description="Stops the server", args = []))
Shell.register(Item(command="db", func=db.main, description="Database management utils", args = [Item(name="action", require=True), Item(name="database", require=True)]))
Shell.register(Item(command="attrfix", func=attrfix.main, description="Fixes attributes for selected database", args = [Item(name="database", require=True)]))
# Shell.register(Item(command="script", func=script.main, desciption="Execute a python script", args = [Item(name="code", require=True)])) #debug feature
Shell.run()
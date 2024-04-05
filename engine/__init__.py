import time
from dataforge import console

#set up logging
from .addons import loggingpatch
console.logging.set_path(f"data/logs/{int(time.time())}.log")
console.logging.start()

#set up exceptions
from .addons import exceptiontrace

#import routes for http api
import router as routes

#initialize discord core
# import discordbot.core

#initialize engine core
from . import core
from . import router
from .shell import core 

#show current release
console.info(f"Running {core.Config.name} Server v{core.Version.Release}")
console.info(f"Using " + ", ".join([f"{key}" for key, _ in core.Version.Using.items()]))

#start http api
router.BPLoader.load() #loads blueprints
router.App.run(host=core.Config.http_host, port=core.Config.http_port, debug=core.Config.http_debug)
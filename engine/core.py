import time
import threading

from dataforge import database
from dataforge import config
from dataforge import console

class Version:
    Release = "1.0.0"
    Using = {
        "HTTPRouter": "latest",
        "DataForge": "v1.1/bluemod"
    }


Config = config.Config("data/config.json")



#Update logs ----------------
threading.Thread(target=console.logging.auto_update).start()

#Database save system --------------
class AutosaveManager:
    def __init__(self, dbs, interval=300):
        self.dbs = dbs
        self.interval = interval
        self.running = True
        self.tag = console.tag(console.COLOR.MAGENTA, "Autosave")
        
        self.thread = threading.Thread(target=self._autosave)
        # self.thread.start()
        
    def _autosave(self):
        time.sleep(5)
        while self.running:
            for db in self.dbs:
                db.save(indent = Config.localhost)
            self.tag.print(f"Saved {len(self.dbs)} databases")
            
            for _ in range(self.interval):
                if not self.running: break
                time.sleep(1)
            
            
    def stop(self):
        self.tag.print("Waiting for service to shutdown")
        self.running = False
        # self.thread.join()
        
        self.tag.print("Saving data")
        for db in self.dbs:
            db.save(indent = Config.localhost)
            
Autosave = AutosaveManager(
    dbs = [

    ]) #disabled -> not used for now
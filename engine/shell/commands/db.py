from dataforge import database
import time

load_request = 0

def main(action=None, dbname=None, *args, **kwargs):
    global load_request
    
    match action:
        case "save":
            db = database.get_instance(dbname)
            if not db:
                return "Database not found"
            
            db.save()
            return "Database saved"
        
        case "load":
            if time.time() - load_request > 10:
                load_request = time.time()
                return "Are you sure you want to load the database? This will overwrite any unsaved changes. Execute the command again to confirm."
            
            db = database.get_instance(dbname)
            if not db:
                return "Database not found"
            
            db.load()
            return "Database loaded"
        
        case _:
            return "Available actions: save, load"
import time
from dataforge import database

schemes = {}

def main(name=None):
    if name == None:
        return "Missing database name, use 'db list' to see available databases"    
        
    db = database.get_instance(name)
    
    scheme = schemes.get(name)
    if not scheme:
        return "No scheme found for this database"
    
    scheme = scheme()
    
    updated_items = 0
    updated_attrs = 0
    started = time.time()
    
    for item in db.content:
        updated = False
        
        #add new attributes
        for key, value in vars(scheme).items():
            
            if not hasattr(item, key):
                setattr(item, key, value)
                updated_attrs += 1    
                updated = True
        
        #delete old attributes
        for key, value in vars(item).items():
            if not hasattr(scheme, key):
                delattr(item, key)
                updated_attrs += 1
                updated = True
                
        if updated:
            updated_items += 1
        
        
            
    return f"Updated {updated_attrs} attributes in total of {updated_items} items, within {time.time() - started:.2f}s"
        
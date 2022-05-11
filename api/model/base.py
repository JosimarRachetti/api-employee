

class BaseDb:
    def __init__(self):
        self.db = ''
    
    def build_query(self, table, **kwargs):
        query = self.db.query(table)
        for key, value in kwargs.items():
            query = query.filter(getattr(table, key)==value)
        return query

    def set_values(self, obj_db, **dic_values):
        for key, value in dic_values.items():
            setattr(obj_db, key, value)
        return obj_db

    def add_db(self, obj_to_add):
        self.db.add(obj_to_add)
        self.flush_action()
        return obj_to_add

    def update_db(self, obj_to_update, **data):
        obj_already_updated = self.set_values(obj_to_update, **data)
        self.flush_action()
        return obj_already_updated

    def delete_db(self, query):
        query.delete()
        self.flush_action()

    def flush_action(self):
        self.db.flush() 
    
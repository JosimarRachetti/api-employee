from database.database import Position
from model.base import BaseDb
from datetime import datetime

class PositionDB(BaseDb):
    def __init__(self, db):
        super().__init__()
        self.db = db

    def new_position(self, **data):
        position = Position()
        position = self.set_values(position, **data)
        position = self.add_db(position)
        return position


    def update_position(self, **data):
        position_to_update = self.find_position(**{"id": int(data['id'])})
        if not len(position_to_update) > 0:
            return position_to_update
        data = {**data, "last_update": str(datetime.now().isoformat())}
        position_already_updated = self.update_db(position_to_update[0], **data)
        return position_already_updated

    def find_position(self, **query):
        query = self.build_query(Position, **query)
        return query.all()
       


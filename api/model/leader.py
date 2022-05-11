from database.database import Leader
from model.base import BaseDb

class LeaderDB(BaseDb):
    def __init__(self, db):
        super().__init__()
        self.db = db

    def new_leader(self, **data):
        leader = Leader()
        leader = self.set_values(leader, **data)
        leader = self.add_db(leader)
        return leader


    def update_leader(self, **data):
        leader_to_update = self.find_leader(**{"id": int(data['id'])})
        if not len(leader_to_update) > 0:
            return leader_to_update
        leader_already_updated = self.update_db(leader_to_update[0], **data)
        return leader_already_updated

    def find_leader(self, **query):
        query = self.build_query(Leader, **query)
        return query.all()
       

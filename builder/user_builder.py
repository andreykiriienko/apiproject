from db_request.db_fabric import DumbDB
from dto.DTO import User, Links, Types
import dataclasses
import json


class UserBuilder:
    def __init__(self):
        self.db = DumbDB()
        self.dto_user = User()
        self.dto_links = Links()
        self.dto_types = Types()

    def get_user(self, user_id):
        user = self.db.get_user_by_id(user_id)
        self.dto_user.id = user_id
        self.dto_user.username = user['username']
        self.dto_user.name = user['name']
        self.dto_user.email = user['email']
        self.dto_user.role = user['role']
        self.dto_user.date_creation = str(user['date_creation'])
        self.dto_user.links = self.fill_links_fields(user_id=user_id)
        return self

    def fill_links_fields(self, user_id):
        links = self.db.get_links_by_user_id(user_id=user_id)
        link_list = []
        for index, item in enumerate(links):
            link_list.append({
                'link_id': item.id,
                'user_id': item.user_id,
                'link': item.link,
                'link_type': self.fill_type_fields(type_id=item.link_type_id)
            })
        return link_list

    def fill_type_fields(self, type_id):
        link_type = self.db.get_type_by_id(type_id=type_id)
        return {'id': link_type['id'], 'type': link_type['type']}

    def to_json(self):
        return json.dumps(dataclasses.asdict(self.dto_user))

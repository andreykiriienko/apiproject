from db_request.db_fabric import DumbDB
import dto.DTO as dto
from dataclasses import asdict
import json


class UserBuilder:
    def __init__(self):
        self.db = DumbDB()
        self.dto_user = dto.User()
        self.dto_links = dto.Links()
        self.dto_types = dto.Types()

    def get_user(self, id):
        user = self.db.get_user_by_id(user_id=id)
        if 'error' not in user:
            self.dto_user.id = id
            self.dto_user.username = user['username']
            self.dto_user.name = user['name']
            self.dto_user.email = user['email']
            self.dto_user.role = user['role']
            self.dto_user.date_creation = str(user['date_creation'])
            self.dto_user.links = self.fill_links_fields(user_id=id)
            return self
        else:
            return self

    def get_user_by_username(self, username):
        user = self.db.get_user_by_username(username=username)
        if 'error' not in user:
            self.dto_user.id = user['id']
            self.dto_user.username = username
            self.dto_user.name = user['name']
            self.dto_user.email = user['email']
            self.dto_user.role = user['role']
            self.dto_user.date_creation = str(user['date_creation'])
            self.dto_user.links = self.fill_links_fields(user_id=user['id'])
            return self
        else:
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
        if self.dto_user.id == 0:
            return json.dumps({'error': ['something went wrong while getting the user']})
        else:
            dto_user = json.dumps(asdict(self.dto_user))
            return json.loads(dto_user)

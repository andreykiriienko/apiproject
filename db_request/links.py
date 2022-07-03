from sqlalchemy.orm import sessionmaker
from dao.DAO import Links
from config import engine


#     TODO:
##      1. Создание ссылки для пользователя (type_id, user_id, link)
##      2. Изменение ссылки для пользователя (link_id, type_id, link)
##      3. Удаление ссылки (link_id)

class DataLinks:

    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_link(self, data):
        user_id = data.get('user_id')
        link_type_id = data.get('link_type_id')
        link = data.get('link')

        links = Links(user_id=user_id, link_type_id=link_type_id, link=link)

        self.session.add(links)
        self.session.commit()
        self.session.close()
        return self

    def get_links_by_user_id(self, user_id):
        links = self.session.query(Links).filter(Links.user_id == user_id).all()
        return links

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

    def create_link(self, data: dict, user_id: int):
        try:
            user_id = user_id
            link_type_id = data.get('link_type_id')
            link = data.get('link')

            links = Links(user_id=user_id, link_type_id=link_type_id, link=link)

            self.session.add(links)
            self.session.commit()
            self.session.close()
            return {'success': f'link with user id: {user_id} - was deleted'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_links_by_user_id(self, user_id):
        links = self.session.query(Links).filter(Links.user_id == user_id).all()
        return links

    def link_update(self, link_id, link: str):
        try:
            self.session.query(Links).filter(Links.id == link_id).update({'link': link})
            self.session.commit()
            return {'success': f'link with id: {link_id} - was update'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def link_delete(self, link_id):
        try:
            id_link = self.session.query(Links).filter(Links.id == link_id).first()

            self.session.delete(id_link)
            self.session.commit()
            return {'success': f'link with id: {id_link} - was deleted'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

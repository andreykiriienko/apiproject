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

    def create_link(self, data: dict):
        try:
            user_id = data.get('user_id')
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
        try:
            links = self.session.query(Links).filter(Links.user_id == user_id).all()
            return links
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_links_by_id(self, link_id):
        try:
            link = self.session.query(Links).filter(Links.id == link_id).first()
            return {'id': link.id, 'user_id': link.user_id, 'link_type_id': link.link_type_id, 'link': link.link}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def link_update(self, data: dict):
        id = data.get('id')
        link = data.get('link')
        link_type_id = data.get('link_type_id')
        try:
            self.session.query(Links).filter(Links.id == id).update({'link': link, 'link_type_id': link_type_id})
            self.session.commit()
            return {'success': f'link with id: {id} - was update'}
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

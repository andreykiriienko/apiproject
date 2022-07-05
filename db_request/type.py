from sqlalchemy.orm import sessionmaker
from dao.DAO import Types
from config import engine


#     TODO:
##      1. Полумение id типа по имени
##      2. Обновление типа по id - (id, type: str)


class DataTypes:

    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_type(self, data: dict):
        try:
            link_type = data.get('link_type')
            types = Types(type=link_type)

            self.session.add(types)
            self.session.commit()
            self.session.close()
            return {'success': f'type with link_type: {link_type} - was created'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_type_by_type_name(self, data: dict):
        name = data.get('link_type')
        link_type = self.session.query(Types).filter(Types.type == name).first()
        return {'id': link_type.id, 'type': link_type.type}

    def get_type_by_id(self, type_id):
        link_type = self.session.query(Types).filter(Types.id == type_id).first()
        return {'id': link_type.id, 'type': link_type.type}

    def type_delete(self, type_id):
        try:
            id_type = self.session.query(Types).filter(Types.id == type_id).first()

            self.session.delete(id_type)
            self.session.commit()
            return {'success': f'type with id: {id_type} - was deleted'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_all(self):
        pass

    def update_type(self, user_id):
        pass

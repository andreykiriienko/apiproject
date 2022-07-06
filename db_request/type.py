from sqlalchemy.orm import sessionmaker
from dao.DAO import Types
from config import engine


class DataTypes:

    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_type(self, data: dict):
        try:
            link_type = data.get('type')
            if 'type' in data:
                link_type_in_db = self.session.query(Types).filter(Types.type == link_type).first()
                if not link_type_in_db:
                    types = Types(type=link_type)
                    self.session.add(types)
                    self.session.commit()
                    self.session.close()
                    return {'success': f'type with type: {link_type} - was created'}
                else:
                    return {'error': f'Duplicat entry with key - type'}
            else:
                return {'error': 'Error with key - type. Key - link_type must be in data'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_type_by_type_name(self, data: dict):
        name = data.get('type')
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

    def update_type(self, data: dict):
        type_id = data.get('id')
        type = data.get('type')

        try:
            self.session.query(Types).filter(Types.id == type_id).update({'type': type})
            self.session.commit()
            return {'success': f'type with id: {type_id} - was update'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

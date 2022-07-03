from sqlalchemy.orm import sessionmaker
from dao.DAO import Types
from config import engine


#     TODO:
##      1. Полумение id типа по имени
##      2. Обновление типа по id - (id, type: str)
##      3. Удаление типа по id


class DataTypes:

    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_type(self, link_type: str):
        types = Types(type=link_type)

        self.session.add(types)
        self.session.commit()
        self.session.close()
        return self

    def get_type_by_id(self, type_id):
        link_type = self.session.query(Types).filter(Types.id == type_id).first()
        return {'id': link_type.id, 'type': link_type.type}

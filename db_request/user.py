from sqlalchemy.orm import sessionmaker
from dao.DAO import Users
from config import engine


#     TODO:
##      1. Полумение Юзера по username
##      2. Удаоение Юзера


class DataUsers:

    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_user(self, data):
        email = data.get('email')
        username = data.get('username')
        last_name = data.get('last_name')
        name = data.get('name')
        password = data.get('password')

        user = Users(email=email, username=username, last_name=last_name,
                     name=name, password=password)

        self.session.add(user)
        self.session.commit()
        self.session.close()
        return self

    def get_user_by_id(self, user_id):
        user = self.session.query(Users).filter(Users.id == user_id).first()
        user_data = {'id': user.id, 'username': user.username, 'name': user.name, 'last_name': user.last_name,
                     'email': user.email, 'role': user.role, 'date_creation': user.date_creation}
        return user_data

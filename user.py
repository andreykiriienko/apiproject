from sqlalchemy.orm import sessionmaker
from DAO import engine
from DTO import User


class DataUsers:

    def __init__(self):
        self.session = sessionmaker(bind=engine)
        self.sess = self.session()
        self.dto = User

    def create_user(self, data):
        email = data.get('email')
        username = data.get('username')
        role = data.get('role')
        last_name = data.get('last_name')
        name = data.get('name')
        password = data.get('password')
        date_creation = data.get('dare_creation')
        links = data.get('links')

        user = User(email=email, username=username, role=role, last_name=last_name,
                    name=name, password=password, date_creation=date_creation,
                    links=links)

        self.sess.add(user)
        self.sess.commit()
        self.sess.close()
        return self

    def get_users_by_username(self, username: str):
        try:
            user = self.sess.quary(User).filter(User.username == username).first()
            self.sess.close()
            return {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password,
                    'role': user.role, 'date_creation': user.date_creation, 'last_name': user.last_name,
                    'links': user.links}
        except Exception as error:
            self.sess.close()
            return {'error': error}

    def get_user_by_id(self, id):
        try:
            user = self.sess.query(User).filter(User.id == id).first()
            self.sess.close()
            return {'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password,
                    'role': user.role, 'date_creation': user.date_creation, 'last_name': user.last_name,
                    'links': user.links}
        except Exception as error:
            self.sess.close()
            return {'error': error}

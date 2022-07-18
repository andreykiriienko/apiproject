from sqlalchemy.orm import sessionmaker
from dao.DAO import Users
from config import engine


class DataUsers:

    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def create_user(self, data):
        try:
            email = data.get('email')
            username = data.get('username')
            last_name = data.get('last_name')
            name = data.get('name')
            password = data.get('password')

            user = Users(email=email, username=username, last_name=last_name,
                         name=name, password=password)

            self.session.add(user)
            self.session.commit()
            return self
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_user_by_id(self, user_id):
        try:
            user = self.session.query(Users).filter(Users.id == user_id).first()
            return {'id': user.id, 'username': user.username, 'name': user.name, 'last_name': user.last_name,
                    'email': user.email, 'role': user.role, 'date_creation': user.date_creation}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_user_by_username(self, username):
        try:
            user = self.session.query(Users).filter(Users.username == username).first()
            return {'id': user.id, 'username': user.username, 'name': user.name, 'last_name': user.last_name,
                    'email': user.email, 'role': user.role, 'date_creation': user.date_creation}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def user_delete(self, user_id):
        try:
            user = self.session.query(Users).filter(Users.id == user_id).first()

            self.session.delete(user)
            self.session.commit()
            return {'success': f'user with id: {user_id} - was deleted'}
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

    def get_all_users(self):
        try:
            users = self.session.query(Users).all()
            users_dict = {}
            for index, user in enumerate(users):
                users_dict[user.id] = {'id': user.id, 'username': user.username, 'name': user.name,
                                       'last_name': user.last_name,
                                       'email': user.email, 'role': user.role, 'date_creation': user.date_creation}
            return users_dict
        except Exception as error:
            return {'error': [error]}
        finally:
            self.session.close()

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime
from config import Base, engine
import pymysql

pymysql.install_as_MySQLdb()


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    role = Column(String(50), default='user')
    date_creation = Column(TIMESTAMP, default=datetime.now())


class Types(Base):
    __tablename__ = 'Types'

    id = Column(Integer, primary_key=True)
    type = Column(String(100), unique=True)


class Links(Base):
    __tablename__ = 'Links'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    link_type_id = Column(Integer, ForeignKey('Types.id'))
    link = Column(String(150), nullable=True)
    user = relationship('Users')
    type_links = relationship('Types')


Base.metadata.create_all(engine)

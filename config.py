from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DB_USERNAME = 'pbbot_apiproject'
DB_PASSWORD = '5(d8H3h)vT'
DB_NAME = 'pbbot_apiproject'
DB_HOST = 'pbbot.mysql.tools'
DB_PORT = ''

engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}', encoding='utf8')
Base = declarative_base()

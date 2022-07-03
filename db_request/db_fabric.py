from db_request.user import DataUsers
from db_request.links import DataLinks
from db_request.type import DataTypes


class DumbDB(DataLinks, DataUsers, DataTypes):
    pass

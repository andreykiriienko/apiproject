from dataclasses import dataclass


@dataclass
class Types:
    id: int = None
    types: str = None


@dataclass
class Links:
    id: int = None
    user_id: int = None
    link: str = None
    # link_type: dict = Types()


@dataclass
class User:
    id: int = None
    username: str = None
    name: str = None
    last_name: str = None
    email: str = None
    role: str = None
    date_creation: str = None
    links: list = Links()
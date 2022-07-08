from dataclasses import dataclass, field
from typing import List


@dataclass()
class Types:
    id: int = field(default_factory=int)
    types: str = field(default='')


@dataclass()
class Links:
    id: int = field(default_factory=int)
    user_id: int = field(default_factory=int)
    link: str = field(default='')


@dataclass()
class User:
    id: int = field(default_factory=int)
    username: str = field(default='')
    name: str = field(default='')
    last_name: str = field(default='')
    email: str = field(default='')
    role: str = field(default='')
    date_creation: str = field(default='')
    links: List[Links] = field(default_factory=list)

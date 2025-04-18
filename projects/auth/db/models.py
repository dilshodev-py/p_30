from dataclasses import dataclass
from typing import Optional

from projects.auth.db.conf import Manager


@dataclass
class User(Manager):
    id : int = None
    first_name : str = None
    username : str = None
    password : str = None

    def is_auth(self):
        user: User | None = User(username=self.username).first()
        assert user , "Username not found"
        assert user.password == self.password , "Not match password"
        return user

    def is_validation(self):
        user: User | None = User(username=self.username).first()
        assert not user , 'Already exists username'
        assert len(self.password) > 4 , "password short !"




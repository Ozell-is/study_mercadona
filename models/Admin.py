import json

from app import db
from utils.PasswordUtils import encode_password


class Admin(db.Model):
    __tablename__ = "Admin"

    _username = db.Column("username", db.String(20), nullable=False, primary_key=True)
    _password = db.Column("password", db.String(150), nullable=False)

    def __init__(self, username: str, password: str):

        self._username = username
        self._password = encode_password(password) \
            .decode(encoding='utf-8')


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    # retour de l'objet python en json
    def to_json(self):
        return self.__str__()

    # conversion de lobjet python en json
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    # renvoi d'un dictionnaire de la classe actuelle
    def __iter__(self):
        yield from {
            "username": self._username,
            "password": self._password
        }.items()

    def __repr__(self):
        return self.__str__()

    # transforme lobjet json en objet python
    @staticmethod
    def from_json(json_dct):
        return Admin(json_dct["username"], json_dct["password"])

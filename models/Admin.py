import json

from app import db

class Admin(db.Model):
    __tablename__ = "Admin"

    _id_admin = db.Column("id_admin", db.Integer, primary_key=True, autoincrement=True)
    _username = db.Column("username", db.String(20), nullable=False)
    _password = db.Column("password", db.String(20), nullable=False)

    def __init__(self, id_admin: int, username: str, password: str):
        self._id_admin = id_admin
        self._username = username
        self._password = password

    @property
    def id_admin(self):
        return self._id_admin

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
            "id_admin": self._id_admin,
            "username": self._username,
            "password": self._password,
        }.items()

    def __repr__(self):
        return self.__str__()

    # transforme lobjet json en objet python
    @staticmethod
    def from_json(json_admin):
        id_admin: int = int(json_admin["id_admin"])
        return Admin(id_admin, json_admin["username"], json_admin["password"])

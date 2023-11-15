import bcrypt

config_bcrypt = bcrypt.gensalt()


def encode_password(password: str) -> bytes:
    return bcrypt.hashpw(bytes(password, encoding="utf-8"), config_bcrypt)


def check_password(hashed_password, provided_password):
    return bcrypt.checkpw(
        provided_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


"""
def check_password(self, password):
    # Comparaison du mot de passe fourni avec le mot de passe hashé stocké
    return bcrypt.checkpw(password.encode('utf-8'), self._password.encode('utf-8'))
"""

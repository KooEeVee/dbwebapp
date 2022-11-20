from db import db
from werkzeug.security import check_password_hash, generate_password_hash


def register(username, password):
    h_password = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":h_password})
        db.session.commit()
    except:
        return False
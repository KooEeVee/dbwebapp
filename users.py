from db import db
from werkzeug.security import check_password_hash, generate_password_hash

def register(username, password):
    h_password = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":h_password})
        db.session.commit()
        return True
    except:
        return False

def login(username, password):
    try:
        sql = "SELECT * FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if check_password_hash(user.password, password):
            return True
    except:
        return False

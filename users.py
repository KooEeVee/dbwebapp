from db import db
from flask import session
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
        if check_password_hash(user["password"], password):
            session["loggedin"] = True
            session["id"] = user["id"]
            session["username"] = user["username"]
            return True
    except:
        return False

def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)


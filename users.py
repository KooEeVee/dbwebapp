from db import db

def register(username, password):
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":password})
        db.session.commit()
    except:
        return False
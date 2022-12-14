from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sqlalchemy import create_engine

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
engine = create_engine(getenv("DATABASE_URL"))

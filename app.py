from flask import Flask
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["MAX_CONTENT_LENGTH"] = 1048576
app.config["UPLOAD_PATH"] = "uploads"

import routes
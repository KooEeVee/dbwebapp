from app import app
import users
import files
from flask import render_template, redirect, request, session
from werkzeug.utils import secure_filename
import os

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    if not users.register(username, password):
        return render_template("error.html", message="Try another username")
    else:
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    if not users.login(username, password):
        return render_template("error.html", message="Username or password failed, try again")
    else:
        return redirect("/dashboard")

@app.route("/logout")
def logout():
    users.logout()
    return render_template("logout.html")

@app.route("/dashboard")
def dashboard():
    if "loggedin" in session:
        filenames = files.get_uploaded_files(session["username"])
        return render_template("dashboard.html", username=session["username"], filenames=filenames)
    else:
        return redirect("/login")

@app.route("/files_upload", methods=["GET", "POST"])
def files_upload():
    if "loggedin" in session:
        if request.method == "GET":
            return render_template("files_upload.html", username=session["username"])
        if request.method == "POST":
            uploaded_file = request.files["file"]
            uploaded_filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], uploaded_filename))
            files.csv_data_to_postgresql(uploaded_filename, session["username"])
            return redirect("/dashboard")
    else:
        return redirect("/login")

@app.route("/tools")
def tools():
    if "loggedin" in session:
        return render_template("tools.html", username=session["username"])
    else:
        return redirect("/login")
import pandas as pd
from db import engine, db
import os
    
def csv_data_to_postgresql(filename, username):
    file_path = f"uploads/{filename}"
    filename_s = filename.replace(".","")
    table_name = f"{username}_{filename_s}"
    df = pd.read_csv(file_path)
    try:
        df.to_sql(table_name, con=engine, if_exists="fail")
        sql = "INSERT INTO user_files (username, filename) VALUES (:username, :filename)"
        db.session.execute(sql, {"username":username, "filename":filename})
        db.session.commit()
        #os.remove(file_path)
        return True
    except:
        return False

def get_uploaded_files(username):
    empty_filelist = []
    try:
        filelist = []
        sql = "SELECT filename FROM user_files WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        files = result.fetchall()
        for row in files:
            filelist.append(row._mapping["filename"])
        return filelist
    except:
        return empty_filelist
    
def get_preview_file(filename, username):
    empty_preview = []
    filename_s = filename.replace(".","")
    table_name = f"{username}_{filename_s}"
    try:
        sql = f"SELECT * FROM {table_name}"
        df = pd.read_sql(sql, con=engine)
        preview = df.head()
        return preview.to_html(header=True, index=None)
    except:
        return empty_preview

def csv_data_to_postgresql_append(filename, username):
    file_path = f"uploads/{filename}"
    filename_s = filename.replace(".","")
    table_name = f"{username}_{filename_s}"
    df = pd.read_csv(file_path)
    try:
        df.to_sql(table_name, con=engine, if_exists="append")
        #os.remove(file_path)
        return True
    except:
        return False

def csv_data_to_postgresql_replace(filename, username):
    filename_s = filename.replace(".","")
    table_name = f"{username}_{filename_s}"
    file_path = f"uploads/{filename}"
    df = pd.read_csv(file_path)
    print(df)
    try:
        df.to_sql(table_name, con=engine, if_exists="replace")
        #os.remove(file_path)
        return True
    except:
        return False
    


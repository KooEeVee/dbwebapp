import pandas as pd
from db import engine, db
import os

def read_csv_headers(filename):
    file_path = f"uploads/{filename}"
    df = pd.read_csv(file_path)
    df_headers = list(df.columns)
    return df_headers
    
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
    empty_files = []
    try:
        sql = "SELECT filename FROM user_files WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        files = result.fetchall()
        return files
    except:
        return empty_files

""" def csv_data_to_postgresql_append(filename, username):
    file_path = f"uploads/{filename}"
    df = pd.read_csv(file_path)
    print(df)
    try:
        df.to_sql(username, con=engine, if_exists="append")
        #os.remove(file_path)
        return True
    except:
        return False

def csv_data_to_postgresql_replace(filename, username):
    file_path = f"uploads/{filename}"
    df = pd.read_csv(file_path)
    print(df)
    try:
        df.to_sql(username, con=engine, if_exists="replace")
        #os.remove(file_path)
        return True
    except:
        return False """
    


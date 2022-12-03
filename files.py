import pandas as pd
from db import engine

def read_csv_headers(filename):
    file_path = f"uploads/{filename}"
    df = pd.read_csv(file_path)
    df_headers = list(df.columns)
    return df_headers
    
def csv_data_to_postgresql():
    df = pd.read_csv("uploads/test2.csv")
    print(df)
    try:
        df.to_sql("pandastest4", con=engine)
        return True
    except:
        return False
    


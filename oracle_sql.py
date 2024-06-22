import pandas as pd
import cx_Oracle
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
pwd = os.getenv('ORACLE_PWD')
oracle_user = os.getenv('ORACLE_USER')
oracle_host = os.getenv('ORACLE_HOST')
oracle_port = os.getenv('ORACLE_PORT')
oracle_sid = os.getenv('ORACLE_SID')

# Update the connection string based on the environment variables
connection_string = f"{oracle_user}/{pwd}@{oracle_host}:{oracle_port}/{oracle_sid}"

conn = cx_Oracle.connect(connection_string)

file_path = Path('D:/sql_data/salesdaily.csv')
cur = conn.cursor()

try:
    df = pd.read_csv(file_path)
    df['datum'] = pd.to_datetime(df['datum'], format='%m/%d/%Y', errors='coerce')  
    datainsertion = [tuple(x) for x in df.values]
    sqt_txt = """
        INSERT INTO test."salesdaily1"
        (datum, "M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06", Year1, Month1, Hour1, "Weekday Name")
        VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)
    """
    cur.executemany(sqt_txt, datainsertion)
    query = "SELECT * FROM salesdaily1"
    cur.execute(query)
    conn.commit()
except Exception as e:
    print(e)
finally:
    cur.close()
    conn.close()

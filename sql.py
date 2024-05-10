import pandas as pd
from sqlalchemy import create_engine 
import urllib.parse 
import pathlib
from pathlib import Path
import os 
from dotenv import load_dotenv
load_dotenv()
pwd=os.getenv('POSTGRES_PWD')
encoded_password = urllib.parse.quote_plus(pwd)

connection_string=f"postgresql://postgres:{encoded_password}@localhost/postgres"

engine=create_engine(connection_string)
conn = engine.connect()


# print(df)
# df.to_sql("artists",con=conn,index=False,if_exists='replace')

for i in os.listdir(Path(r'C:\Users\santh\Downloads\paintings')):
    df =pd.read_csv(Path(fr'C:\Users\santh\Downloads\paintings\{i}'))
    filename=i.split('.')[0]
    df.to_sql(f'{filename}',con=conn,index=False,if_exists='replace')

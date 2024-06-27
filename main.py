import pandas as pd
import numpy as np
import pendulum
import os
import pyodbc
from airflow.models import TaskInstance

server = os.getenv('SERVER_NAME')
database = os.getenv('DB_NAME')
username = os.getenv('USER')
password = os.getenv('DB_PASSWORD')

sql_server = "FreeTDS"
connection_string = 'DRIVER={'+ sql_server +'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password + ';TrustServerCertificate=yes;'

def main():
    df_code = pd.read_sql('SELECT TRIM([TICKER]), [IsShares] FROM metadata ORDER BY TICKER',cnxn)
    return df_code

main()
import pandas as pd
import numpy as np
import pendulum
import os
import pyodbc
from airflow.models import TaskInstance

server = os.environ['SERVER_NAME']
database = os.environ['DB_NAME']
username = os.environ['USER']
password = os.environ['DB_PASSWORD']

sql_server = "FreeTDS"
connection_string = 'DRIVER={'+ sql_server +'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password + ';TrustServerCertificate=yes;'

def main():

    cnxn = pyodbc.connect(connection_string, autocommit=True)
    df_code = pd.read_sql('SELECT TRIM([TICKER]) AS TICKER, [IsShares] FROM [FINANCE].[DBO].[metadata] ORDER BY TICKER',cnxn)
    print(df_code.to_json())

main()
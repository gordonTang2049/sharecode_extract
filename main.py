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
ti = os.environ['TASK_INSTANCE']

# task_id = os.environ['TASK_ID']
# dag_id = os.environ['DAG_ID']
# exec_date = os.environ['EXECUTION_DATE']


sql_server = "FreeTDS"
connection_string = 'DRIVER={'+ sql_server +'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password + ';TrustServerCertificate=yes;'

def main():

    cnxn = pyodbc.connect(connection_string, autocommit=True)
    df_code = pd.read_sql('SELECT TRIM([TICKER]), [IsShares] FROM [FINANCE].[DBO].[metadata] ORDER BY TICKER',cnxn)
    print(df_code)
    # ti = TaskInstance(
    #     task=task_id, 
    #     dag_id=dag_id, 
    #     execution_date=exec_date);
    ti.xcom_push(df_code)

main()
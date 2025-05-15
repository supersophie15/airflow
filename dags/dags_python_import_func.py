from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from commom.commom_func import get_sftp 

#python이 클래스를 가져오는 경로를 plugins를 인식하도록 설정해주어야함. 
#airflow는 plugins 폴더까지 python path 로 잡는다.> 따라서 맨 앞에 plugins를 작성하면 안된다. 이때 코드에러가 나기 때문에 .env 파일을 하나 작성한다. 

with DAG(
    dat_id='dags_python_import_func',
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id='task_get_sftp',
        python_callable=get_sftp
    )
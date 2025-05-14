from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
import random


#DAG 클래스 기본 정의하기 - 모든 DAG 파일에 작성해야함
with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023,3,1,tz="Asia/Seoul"), 
    catchup=False,
) as dag:
    def select_fruit(): #함수정의
        fruit = ['APPLE','ORANGE','AVOCADO'] #정의 내용은 같은 들여쓰기에 작성
        rand_int = random.randint(0,3)
        print(fruit[rand_int])
    py_t1 = PythonOperator(
        task_id='py_t1'
        python_callable=select_fruit
    )

    py_t1
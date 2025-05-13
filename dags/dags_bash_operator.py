from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

#DAG 클래스 기본 정의하기 - 모든 DAG 파일에 작성해야함
with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021,1,1,tz="Asia/Seoul"), #tz=timezone, 세계표준 UTC (한국보다 9시간 느림)
    catchup=False,
) as dag:
    bash_t1 = BashOperator( #task 객체명
        task_id="bash_t1",
        bash_command="echo whoami",  #echo = print와 비슷
    )

    bash_t2 = BashOperator( 
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",  #HOSTNAME = wsl의 터미널 네임
    )

    bash_t1 >> bash_t2


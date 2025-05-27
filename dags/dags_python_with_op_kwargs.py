from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import pythonOperator
from common.common_func import regist2


with DAG(
    dag_id="dags/dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023,3,1,tz="Asia/Seoul"), 
    catchup=False,
) as dag:
    
    # 일반적인 python operator
    # def select_fruit(): #함수정의
    #     fruit = ['APPLE','ORANGE','AVOCADO'] #정의 내용은 같은 들여쓰기에 작성
    #     rand_int = random.randint(0,3)
    #     print(fruit[rand_int])

    # py_t1 = PythonOperator(
    #     task_id='py_t1',
    #     python_callable=select_fruit #정의된 함수를 불러옴옴      
    # )

    # py_t1



    #외부함수 불러오기
    regist2_t1 = pythonOperator(
        task_Id = 'regist2_t1',
        python_callable=regist2,
        op_args =['sjpark','woman','kr','seoul'],
        op_kwargs = {'email':'sujeong.bak@gmail.com','phone':'01023456789'}        
    )

    regist2_t1 
        

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_print():
    return "Log by Vokno"

dag = DAG(
    'hello_world', 
    description='Hello world DAG',
    schedule_interval="@once",
    start_date=datetime(2022, 1, 1),
    catchup = False,
)

hello_operator = PythonOperator(task_id='hello_task', python_callable=hello_print, dag=dag)

hello_operator
# my_dag.py

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Define default_args
default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
)

# Define tasks
start_task = DummyOperator(task_id='start_task', dag=dag)

def my_python_function():
    # Your Python code here
    print("Hello, Airflow!")

python_task = PythonOperator(
    task_id='python_task',
    python_callable=my_python_function,
    dag=dag,
)

end_task = DummyOperator(task_id='end_task', dag=dag)

# Define task dependencies
start_task >> python_task >> end_task

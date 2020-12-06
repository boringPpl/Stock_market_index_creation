from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'Steven Chia',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['stevenchia56@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(days=1),
}

dag = DAG('Testing_Airflow', default_args=default_args, description='Testing out Airflow', schedule_interval=timedelta(minutes=1))

# t1, t2, t3 and t4 are examples of tasks created using operators

t1 = BashOperator(
    task_id='task_1',
    bash_command='python /usr/local/airflow/dags/scripts/task_1.py',
    dag=dag)

t2 = BashOperator(
    task_id='task_2',
    bash_command='python /usr/local/airflow/dags/scripts/task_2.py',
    dag=dag)

t3 = BashOperator(
    task_id='task_3',
    bash_command='python /usr/local/airflow/dags/scripts/task_3.py',
    dag=dag)

t1 >> t2 >> t3

dag.doc_md = __doc__

t1.doc_md = """\
#### Task Documentation
What does this part do?
![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
"""

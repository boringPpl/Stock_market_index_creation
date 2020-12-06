import pandas as pd

df = pd.read_csv('/usr/local/airflow/dags/files/first.csv')
df['second column'] = ['a', 'b', 'c']
df.to_csv('/usr/local/airflow/dags/files/second.csv', index=False)

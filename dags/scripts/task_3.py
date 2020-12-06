import pandas as pd

df = pd.read_csv('/usr/local/airflow/dags/files/second.csv')
df['third column'] = ['4', '5', '6']
df.to_csv('/usr/local/airflow/dags/files/third.csv', index=False)

import pandas as pd

df = pd.DataFrame([1, 2, 3], columns=['first column'])
df.to_csv('/usr/local/airflow/dags/files/first.csv', index=False)

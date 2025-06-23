from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def saludo():
    print("¡Hola Emiliano, tu DAG funciona!")

with DAG(
    dag_id="primer_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    tarea = PythonOperator(
        task_id="saludar",
        python_callable=saludo
    )

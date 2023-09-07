from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.filesystem import FileSensor
from extract import download_csv_from_s3
from datetime import datetime, timedelta
from transform import transformation
from load import s3_load

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG("uber_etl", start_date=datetime(2021, 1, 1),
         schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=download_csv_from_s3
    )

    is_raw_file_available = FileSensor(
        task_id="is_raw_file_available",
        fs_conn_id="file_path",
        filepath="raw.csv",
        poke_interval=5,
        timeout=20
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transformation
    )

    load = PythonOperator(
        task_id='load',
        python_callable=s3_load
    )

extract >> is_raw_file_available >> transform
transform >> load

import os

import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import timedelta


default_args = {
    'owner': 'airflow',
    'email': ['airflow@example.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


with DAG(
    dag_id="generate_data",
    default_args=default_args,
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily",
) as dag:

    get_data = DockerOperator(
        image="airflow-download",
        task_id="get_data_1",
        do_xcom_push=False,
	command = "--train_dir /data/raw/ --output_dir /data/raw/",
        volumes=['/d/katka/MADE/semester2/ML_in_production/airflow/airflow-examples/data:/data'],
    )

    notify = BashOperator(
        task_id="notify",
        bash_command=f'echo "new rows of data generated ... "',
    )

    get_data >> notify

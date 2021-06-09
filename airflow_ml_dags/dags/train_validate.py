import os

import airflow
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator


RAW_DATA_PATH = "data/raw/data.csv"
RAW_TARGET_PATH = "data/raw/target.csv"


with DAG(
    dag_id="train_val",
    start_date=airflow.utils.dates.days_ago(21),
    schedule_interval="@weekly",
) as dag:
    wait_for_features = FileSensor(
        task_id="wait-for-features", poke_interval=5, retries=5, filepath=RAW_DATA_PATH
    )

    wait_for_target = FileSensor(
        task_id="wait-for-target", poke_interval=5, retries=5, filepath=RAW_TARGET_PATH
    )

    preprocess = DockerOperator(
        image="airflow-preprocess",
        task_id="preprocess",
        do_xcom_push=False,
        command = '--input-dir /data/raw/ --output-dir /data/processed/{{ ds }}',
        volumes=['/d/katka/MADE/semester2/ML_in_production/airflow/airflow-examples/data:/data'],
    )

    split = DockerOperator(
        image="airflow-split",
        task_id="split",
        do_xcom_push=False,
        command = '--input-dir /data/processed/{{ ds }} --output-dir /data/splitted/{{ ds }}',
        volumes=['/d/katka/MADE/semester2/ML_in_production/airflow/airflow-examples/data:/data'],
    )

    train = DockerOperator(
        image="airflow-train",
        task_id="train",
        do_xcom_push=False,
        command = '--input-dir /data/splitted/{{ ds }} --output-dir /data/model/{{ ds }}',
        volumes=['/d/katka/MADE/semester2/ML_in_production/airflow/airflow-examples/data:/data'],
    )

    validate = DockerOperator(
        image="airflow-validate",
        task_id="validate",
        do_xcom_push=False,
        command = '--input-dir /data/splitted/{{ ds }} --model-dir /data/model/{{ ds }} ',
        volumes=['/d/katka/MADE/semester2/ML_in_production/airflow/airflow-examples/data:/data'],
    )

    notify = BashOperator(
        task_id="notify",
        bash_command=f'echo "Model train and validated ... "',
    )

    (
        [wait_for_features, wait_for_target]
        >> preprocess
        >> split
        >> train
        >> validate
        >> notify
    )

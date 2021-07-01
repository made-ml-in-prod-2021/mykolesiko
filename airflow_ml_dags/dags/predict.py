import os

import airflow
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.models import Variable


                                                 
model_dir = Variable.get("MODEL_DIR")
if (model_dir is None):
	model_dir = "data/model/{{ ds }}/"


MODEL_PATH = model_dir  + "model.pkl"
TEST_DATA_PATH = "data/raw/test_data.csv"


with DAG(
    dag_id="predict",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily",
) as dag:

    wait_for_data = FileSensor(
        task_id="wait-for-data", poke_interval=10, retries=5, filepath=TEST_DATA_PATH
    )

    wait_for_model = FileSensor(
        task_id="wait-for-model", poke_interval=10, retries=5, filepath=MODEL_PATH
    )

    predict = DockerOperator(
        image="airflow-predict",
        task_id="predict",
        do_xcom_push=False,
        command = f'--input-dir /data/raw/ --model-dir /{model_dir} --output-dir /data/predicted/',
        volumes=['/d/katka/MADE/semester2/ML_in_production/airflow/airflow-examples/data:/data'],
    )

    # parallel sensors
    [wait_for_model, wait_for_data] >> predict

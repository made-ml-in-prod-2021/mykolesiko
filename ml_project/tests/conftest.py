    #from src import implement_pipeline
import os
import pytest
import logging
import sys
from src.implement_pipeline import model_creation_pipeline
from src.model import ModelClass
from src.constants import DATA_DIR, DATA_RAW_DIR
from src.data import generate_data
from src.logs import setup_logging


from marshmallow_dataclass import class_schema
import yaml

from dataclasses import dataclass, field
from typing import List, Optional, Any



TEST_PATH = "tests"
TEST_DATA_PATH = "tests"
TEST_CONFIG_YAML = "model_test.yaml"
TEST_LOG_YAML = "logging_default.yaml"
TRAIN_FILE = "heart.csv"
TEST_FILE = "test.csv"
TRANSFORMER_FILE = "transformer.pkl"
MODEL_PATH = "models"
TEST_MODEL_FOLDER = "test"
NUM_ROWS = 100


#@dataclass()
#class PytestConfigParams:
#    TEST_PATH: str
#    TEST_DATA_PATH: str
#    TEST_CONFIG_YAML : str
#    TRAIN_FILE : str
#    TEST_FILE : str
#    TRANSFORMER_FILE: str
#    MODEL_PATH: str
#    TEST_MODEL_FOLDER: str

#@pytest.fixture()
#def params() -> PytestConfigParams:
#   ConfigSchema = class_schema(PytestConfigParams)
#    path = os.path.join(os.getcwd(), TEST_PATH)
#    with open(path, "r") as config:
#           schema = ConfigSchema()
#           return schema.load(yaml.safe_load(config))


@pytest.fixture()
def test_data_path() -> str:
    path = os.path.join(os.getcwd(), TEST_DATA_PATH)
    if (not os.path.exists(path)):
        os.mkdir(path)
    return path


@pytest.fixture()
def test_path() -> str:
    path = os.path.join(os.getcwd(), TEST_DATA_PATH)
    return path

@pytest.fixture()
def test_config_yaml() -> str:
    path = os.path.join(os.getcwd(), TEST_DATA_PATH, TEST_CONFIG_YAML)
    assert (os.path.exists(path))
    return path


@pytest.fixture()
def test_model_path(test_config_yaml : str) -> str:
    params, model = model_creation_pipeline(test_config_yaml)
    return model.path

@pytest.fixture()
def train_data_path():
    return os.path.join(DATA_DIR, DATA_RAW_DIR, TRAIN_FILE)


@pytest.fixture()
def test_data(train_data_path: str) -> str:
    test_file = os.path.join(os.getcwd(), TEST_DATA_PATH, TEST_FILE)
    data = generate_data(train_data_path, NUM_ROWS, test_file)
    assert os.path.exists(test_file)
    return test_file

@pytest.fixture()
def transformer_path() -> str:
    file = os.path.join(os.getcwd(), MODEL_PATH, TEST_MODEL_FOLDER, TRANSFORMER_FILE)
    return file


@pytest.fixture()
def prediction_path() -> str:
    file = os.path.join(os.getcwd(), TEST_PATH)
    return file

@pytest.fixture()
def logger():
    setup_logging(
        TEST_LOG_YAML,
        os.path.join(os.getcwd(), TEST_PATH, "test.log"),
    )
    logger_test = logging.getLogger("test")
    return logger_test



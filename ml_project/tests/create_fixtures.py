from src import implement_pipeline
import os

TEST_PATH = "tests/"
TEST_DATA_PATH = "tests/"
TEST_CONFIG_YAML = "tests/model_test.yaml"


@pytest_fixture
def test_data_path() -> str:
    if (not os.path.exists(TEST_DATA_PATH)):
        os.mkdir(TEST_DATA_PATH)
    return TEST_DATA_PATH


@pytest_fixture
def test_path() -> str:
    return TEST_PATH

@pytest_fixture
def test_config_yaml() -> str:
    assert (os.path.exists(TEST_CONFIG_YAML))
    return TEST_CONFIG_YAML


@pytest_fixture
def test_model_path(test_config_yaml : str) -> str:
    model = model_creation_pipeline(test_config_yaml)
    return model.path
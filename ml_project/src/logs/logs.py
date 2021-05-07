import logging
import yaml
import logging.config
from  src.utils import get_path
from src.constants import MODELS_DIR, CONFIG_DIR
import os

LOGGER_NAME = "train"
LOGGER_YAML_DEFAULT = "logging_default.yaml"
logger = logging.getLogger(LOGGER_NAME)


def setup_logging(log_yaml: str, log_file_path: str):
    """Setups logging configurations"""
    path = os.path.join(os.getcwd(), CONFIG_DIR, log_yaml)
    with open(path) as config:
        dict_yaml = yaml.safe_load(config)
        dict_yaml['handlers']['file_handler']['filename'] = log_file_path
        #print(dict_yaml)
        logging.config.dictConfig(dict_yaml)

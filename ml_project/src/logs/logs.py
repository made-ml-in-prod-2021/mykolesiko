import logging
import yaml
import logging.config

LOGGER_NAME = "train"
logger = logging.getLogger(LOGGER_NAME)


def setup_logging(log_yaml_path):
    """Setups logging configurations"""
    with open(log_yaml_path) as config:
        logging.config.dictConfig(yaml.safe_load(config))


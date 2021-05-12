"""
    Module for logging configuration
"""
import logging
import yaml
import logging.config

from dataclasses import dataclass, field, MISSING
from typing import List, Optional, Any
from marshmallow_dataclass import class_schema
from src.utils import get_path
from src.constants import MODELS_DIR, CONFIG_DIR
import os

LOGGER_NAME = "train"
LOGGER_YAML_DEFAULT = "logging_default.yaml"
logger = logging.getLogger(LOGGER_NAME)

# version: 1
# formatters:
#     simple:
#         class: logging.Formatter
#         format: "%(levelname)s: %(message)s"
# handlers:
#     file_handler:
#         class: logging.FileHandler
#         filename: train.log
#         level: INFO
#         formatter: simple
# loggers:
#      train:
#         level: INFO
#         handlers: [file_handler]
#         propagate: no
@dataclass()
class Formatter:
    """

    """
    class1: str
    format: str


@dataclass()
class Formatters:
    """

    """
    simple: Formatter = MISSING


@dataclass()
class Handler:
    """

    """
    class1 : str
    filename : str
    level: str
    formatter : str


@dataclass()
class Handlers:
    """

    """
    file_handler: Handler = MISSING


@dataclass()
class Logger:
    level :str
    handlers : List[str]
    propagate: bool



@dataclass()
class Loggers:
    """

    """
    train: Logger = MISSING



@dataclass()
class LogConfigParams:
    """
            Params of logs yaml configuration
    """
    version : int
    formatters: Formatters
    handlers: Handlers
    loggers: Loggers

ConfigSchema = class_schema(LogConfigParams)

def setup_logging(log_yaml: str, log_file_path: str):
    """Setups logging configurations"""
    path = os.path.join(os.getcwd(), CONFIG_DIR, log_yaml)
    with open(path) as config:
        dict_yaml = yaml.safe_load(config)
        dict_yaml["handlers"]["file_handler"]["filename"] = log_file_path
        logging.config.dictConfig(dict_yaml)

    #with open(path, "r") as config:
    #    schema = ConfigSchema()
    #    params = schema.load(yaml.safe_load(config))
    #    params.handlers.file_handler.filename = log_file_path
    #    print(params.__dict__)
    #    logging.config.dictConfig(params.__dict__)



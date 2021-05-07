import json
import logging
import os

import pickle
import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys

import click
import pandas as pd
import sys


from src.config import read_training_config_params, TrainingConfigParams
from src.features import create_target, TransformerClass
from src.model import ModelClass
from src.logs import setup_logging, logger
from src.utils import get_path
from src.constants import MODELS_DIR, CONFIG_DIR, LOGS_DIR, DATA_DIR, DATA_RAW_DIR
from src.data import split_train_val_data





def setup_parser(parser):
    """Setups parser"""
    # parser.set_defaults(callback=callback_analytics)

    parser.add_argument(
        "--config", "-c",
        required=True,
        default=True,
        help="name of config file with path, default path is ./configs/config.yaml",
        metavar="FPATH",
    )

    parser.add_argument(
        "--logs", "-l",
        required=False,
        default=True,
        help="name of logs config file, default path is in model config file",
        metavar="FPATH",
    )


def model_pipeline(params: TrainingConfigParams):
    ### implement all pipeline to get the model ###
    logger.info(f"start train pipeline with params {params}")
    model_folder = os.path.join(os.getcwd(), MODELS_DIR, params.model_folder)
    if (not os.path.exists(model_folder)) :
        os.mkdir(model_folder)

    data = pd.read_csv(os.path.join(DATA_DIR, DATA_RAW_DIR, params.input_data_file))
    logger.info(f"data.shape is {data.shape}")

    logger.info(f"transform the features {params.feature_params}")
    transformer = TransformerClass()
    data_processed = transformer.fit_transform(data, params.feature_params)
    transformer.save(os.path.join(os.getcwd(), MODELS_DIR, params.model_folder, params.transformer_params.file))
    target = create_target(data, params.feature_params)

    logger.info(f"splitted data {params.splitting_params}")
    train_data, val_data, y_train, y_test = split_train_val_data(
        data_processed, target, params.splitting_params
    )

    logger.info(f"train_data.shape is {train_data.shape}")
    logger.info(f"val_data.shape is {val_data.shape}")

    logger.info(f"created model  {params.model_params}")
    model = ModelClass()

    logger.info(f"train model")
    model.train(train_data, y_train, params.model_params)

    logger.info(f"predict values")
    predicts = model.predict(val_data)  #

    metrics = model.evaluate(predicts, y_test)
    logger.info(f"metrics are  {metrics}")

    with open(os.path.join(os.getcwd(), MODELS_DIR, params.model_folder, params.metric_file), "w") as metric_file:
        json.dump(metrics, metric_file)

    model.serialize_model(os.path.join(os.getcwd(), MODELS_DIR, params.model_folder, params.model_file))

    return model


# @click.command(name="train_pipeline")
# @click.argument("config_path")
def model_creation_pipeline(config_path: str):
    params = read_training_config_params(get_path(CONFIG_DIR, config_path))
    setup_logging(params.logging_config, os.path.join(os.getcwd(), MODELS_DIR, params.model_folder, "train.log"))
    model = model_pipeline(params)
    return params, model


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="start and train the model",
        description="pipeline for training different models on data of heart desease",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()

    # arguments.callback(arguments)

    params, model = model_creation_pipeline(arguments.config)
    #print(metrics)

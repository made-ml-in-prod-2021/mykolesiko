import json
import logging

import pickle
import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys

import click
import pandas as pd
import sys

from src.config import read_training_config_params, TrainingConfigParams
from src.features import create_feature_array, create_target, create_transformer, split_train_val_data
from src.model import ModelClass
from src.logs import setup_logging, logger





def setup_parser(parser):
    """Setups parser"""
    #parser.set_defaults(callback=callback_analytics)

    parser.add_argument(
        "--config", "-c",
        required=True,
        default=None,
        help="name of config file with path, default path is ../configs/config.yaml",
        metavar="FPATH",
    )
    
    parser.add_argument(
        "--logs", "-l",
        required=True,
        default=None,
        help="name of logs config file, default path is ../configs/logs.yaml",
        metavar="FPATH",
    )




def model_pipeline(params: TrainingConfigParams ):
    logger.info(f"start train pipeline with params {params}")
    data = pd.read_csv(params.input_data_path)
    logger.info(f"data.shape is {data.shape}")

    logger.info(f"transform the features {params.feature_params}")
    transformer = create_transformer(params.feature_params)
    data_processed = create_feature_array(transformer,  data)
    target = create_target(data, params.feature_params)

    logger.info(f"splitted data {params.splitting_params}")
    train_data, val_data, y_train, y_test = split_train_val_data(
        data_processed, target, params.splitting_params
    )

    logger.info(f"train_data.shape is {train_data.shape}")
    logger.info(f"val_data.shape is {val_data.shape}")

    logger.info(f"created model  {params.model_params}")
    model = ModelClass(params.model_params)

    logger.info(f"ctrain model")
    model.train(train_data, y_train)

    logger.info(f"predict values")
    predicts = model.predict(val_data)#

    metrics = model.evaluate(predicts, y_test)
    logger.info(f"metrics are  {metrics}")
 
    with open(params.metric_path, "w") as metric_file:
        json.dump(metrics, metric_file)
    
    model.serialize_model(params.output_model_path)

    return metrics


#@click.command(name="train_pipeline")
#@click.argument("config_path")
def model_creation_pipeline(config_path: str):
    params = read_training_config_params(config_path)
    model_pipeline(params)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="start and train the model",
        description="pipeline for training different models on data of heart desease",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    setup_logging(arguments.logs)
    #arguments.callback(arguments)

    metrics = model_creation_pipeline(arguments.config)
    print (metrics)

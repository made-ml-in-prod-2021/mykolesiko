import json
import logging
import sys

import click
import pandas as pd



#from ml_code.config import read_training_config_params, split_train_val_data
#from ml_code.features import create_feature_array, create_target, create_transformer
#from ml_example.model import ModelClass

from src.config import read_training_config_params, split_train_val_data
from src.features import create_feature_array, create_target, create_transformer
from src.model import ModelClass


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def setup_parser(parser):
    """Setups parser"""
    #parser.set_defaults(callback=callback_analytics)

    parser.add_argument(
        "--config",
        required=True,
        default=None,
        help="name of config file with path, default path is ../configs/config.yaml",
        metavar="FPATH",
    )
    






def model_creation_pipeline(training_pipeline_params: TrainingPipelineParams):
    logger.info(f"start train pipeline with params {training_pipeline_params}")
    data = pd.read_csv(params.input_data_path)
    logger.info(f"data.shape is {data.shape}")

    transformer = create_transformer(params.feature_params)
    data_processed = create_feature_array(transformer,  data)
    target = create_target(data, params.feature_params)



    train_data, val_data, y_train, y_test = split_train_val_data(
        data_processed, target,TrainingConfigParams.splitting_params 
    )

    logger.info(f"train_df.shape is {train_data.shape}")
    logger.info(f"val_df.shape is {val_data.shape}")

    #transformer = build_transformer(training_pipeline_params.feature_params)
    #transformer.fit(train_df)
    #train_features = make_features(transformer, train_df)
    #train_target = extract_target(train_df, training_pipeline_params.feature_params)

    model = ModelClass(params.model_params)
    model.train(train_data, y_train)#, training_pipeline_params.train_params   )
    predicts = model.predict(val_data)#

    metrics = model.evaluate(predicts, y_test)
    print(metrics)
 
    with open(params.metric_path, "w") as metric_file:
        json.dump(result, metric_file)
    
    model.serialize_model(params.output_model_path)

    return path_to_model, metrics


#@click.command(name="train_pipeline")
#@click.argument("config_path")
def model_creation_pipeline(config_path: str):
    params = read_training_config_params(config_path)
    model_create_pipeline(params)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="start and train the model",
        description="pipeline for training different models on data of heart desease",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    #arguments.callback(arguments)

    model_creation_pipeline(arguments.config)

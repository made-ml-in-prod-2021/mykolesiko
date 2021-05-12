import pandas as pd
import os

from src.model import ModelClass
from src.features import TransformerClass, create_target
from src.logs import logger
from src.constants import CONFIG_DIR
from src.config import read_training_config_params



def predict(data_path: str, config_path: str,  model_path: str, transformer_path: str, save_path: str):
    logger.info(f"read config data from {config_path}")
    params = read_training_config_params(config_path)

    logger.info(f"start predict data from {data_path}, model from {model_path}")
    model = ModelClass()

    logger.info(f"load transformer from  {transformer_path}")
    transformer = TransformerClass()

    sklearn_model = model.load(model_path)
    logger.info(f"load model: {sklearn_model}")

    data = pd.read_csv(data_path)

    logger.info(f"read data shape: {data.shape}")

    transformer.load(transformer_path)
    data_processed = transformer.transform(data)
    predictions = model.predict(data_processed)
    data_new = data.copy()
    data_new[params.feature_params.target] = predictions
    data_new.to_csv(os.path.join(os.getcwd(), save_path, "prediction.csv"))
    return data_new

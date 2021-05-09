import pandas as pd
import os

from src.model import ModelClass
from src.features import TransformerClass, create_target
from src.logs import logger


def predict(data_path: str, model_path: str, transformer_path: str, save_path: str):

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
    data_new["target"] = predictions
    data_new.to_csv(os.path.join(os.getcwd(), save_path, "prediction.csv"))
    print(data_new.head())
    return data_new

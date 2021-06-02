import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from typing import Dict, Union
from src.config import ModelParams
from src.model import ModelClass
from src.predict import predict
#from tests.conftest import logger_test
#from src.logs import setup_logging





def test_load_model(test_model_path, logger):
    logger.info(f"test_load_model")
    model = ModelClass()
    sklearn_model = model.load(test_model_path)
    params1 = sklearn_model.get_params()
    logger.info(f"params of loaded model {params1}")
    assert params1['max_iter'] == 100
    assert params1['solver'] == 'liblinear'

def test_predict(test_data:str, test_config_yaml: str, test_model_path: str, transformer_path:str, prediction_path: str, logger):
    logger.info(f"test_predict")
    prediction  = predict(test_data, test_config_yaml, test_model_path, transformer_path, prediction_path)
    logger.info(f"shape of prediction {prediction}")
    assert prediction.shape == (100, 14)


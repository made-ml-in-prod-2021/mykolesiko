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


def test_load_model(test_model_path):
    model = ModelClass()
    sklearn_model = model.load(test_model_path)
    params1 = sklearn_model.get_params()
    assert params1['max_iter'] == 100
    assert params1['solver'] == 'liblinear'

def test_predict(test_data:str, test_model_path: str, transformer_path:str, prediction_path: str):
    prediction  = predict(test_data, test_model_path, transformer_path, prediction_path)
    assert prediction.shape == (100, 14)


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

#ModelType = Union[RandomForestClassifier, LogisticRegression]


# class ModelClass:
#
#     def __init__(self):
#         pass
#
#     def load(self, path):
#         with open(path, "rb") as f:
#             self.model = pickle.load(f)
#         return self.model
#
#     def train(self, features: pd.DataFrame, target: pd.Series, params: ModelParams) -> ModelType:
#         print(self.params.model_type)
#         self.params = params
#         if self.params.model_type == "RandomForestClassifier":
#             self.model = RandomForestClassifier(
#                 n_estimators=600,
#             ).fit(features, target)
#         elif self.params.model_type == "GradientBoostingClassifier":
#             self.model = GradientBoostingClassifier(n_estimators=100).fit(features, target)
#         else:
#             self.model = LogisticRegression(max_iter=1000).fit(features, target)
#
#         return self.model
#
#     def predict(self, features: pd.DataFrame) -> np.ndarray:
#         predicts = self.model.predict(features)
#         return predicts
#
#     def evaluate(self, predicts: np.ndarray, target: pd.Series) -> Dict[str, int]:
#         return {
#             "accuracy": accuracy_score(target, predicts)
#         }
#         "rmse": mean_squared_error(target, predicts, squared=False),
#         "mae": mean_absolute_error(target, predicts),
    #
    # def serialize_model(self, output: str) -> str:
    #     with open(output, "wb") as f:
    #         pickle.dump(self.model, f)
    #     return output
#
def test_load_model(test_model_path):
    model = ModelClass()
    sklearn_model = model.load(test_model_path)
    params1 = sklearn_model.get_params()
    print(params1)
    assert params1['max_iter'] == 100
    assert params1['solver'] == 'liblinear'

def test_predict(test_data:str, test_model_path: str, transformer_path:str, prediction_path: str):
    prediction  = predict(test_data, test_model_path, transformer_path, prediction_path)
    assert prediction.shape == (100, 14)


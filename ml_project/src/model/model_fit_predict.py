import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from typing import Dict, Union
from src.config import ModelParams

ModelType = Union[RandomForestClassifier, LogisticRegression]


class ModelClass:
    def __init__(self):
        pass

    def load(self, path):
        print(path)
        with open(path, "rb") as f:
            self.model = pickle.load(f)
        return self.model

    def train(self, features: pd.DataFrame, target: pd.Series, params: ModelParams) -> ModelType:
        self.params = params
        self.features = features
        self.target = target


        print(self.params.model_type)
        self.params = params
        if self.params.model_type == "RandomForestClassifier":
            self.model = RandomForestClassifier(
                n_estimators=600,
            ).fit(features, target)
        elif self.params.model_type == "GradientBoostingClassifier":
            self.model = GradientBoostingClassifier(n_estimators=100).fit(features, target)
        else:
            self.model = LogisticRegression(max_iter=1000).fit(features, target)

        return self.model

    def predict(self, features: pd.DataFrame) -> np.ndarray:
        self.predicts = self.model.predict(features)
        return self.predicts

    def evaluate(self, predicts: np.ndarray, target: pd.Series) -> Dict[str, int]:
        return {
            "accuracy": accuracy_score(target, predicts)
        }
        # "rmse": mean_squared_error(target, predicts, squared=False),
        # "mae": mean_absolute_error(target, predicts),

    def serialize_model(self, output: str) -> str:
        with open(output, "wb") as f:
            pickle.dump(self.model, f)
        self.path = output
        return output




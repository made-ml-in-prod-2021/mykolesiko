"""
    ModelClass
"""
import pickle
from typing import Dict, Union
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

import pandas as pd
import numpy as np

from src.config import ModelParams
from sklearn import metrics

ModelType = Union[RandomForestClassifier, LogisticRegression]


class ModelClass:
    """
        ModelClass
    """
    def __init__(self):
        pass

    def load(self, path):
        """
            load from file
        """

        with open(path, "rb") as f:
            self.model = pickle.load(f)
        return self.model

    def train(self, features: pd.DataFrame, target: pd.Series,\
              model_params: ModelParams, metric_params: list) -> ModelType:
        self.features = features
        self.target = target

        self.model_params = model_params
        self.metric_params = metric_params
        if self.model_params.model_type == "RandomForestClassifier":
            self.model = RandomForestClassifier(
                n_estimators=model_params.n_estimators,
            ).fit(features, target)
        elif self.model_params.model_type == "GradientBoostingClassifier":
            self.model = GradientBoostingClassifier(
                n_estimators=model_params.n_estimators
            ).fit(features, target)
        else:
            self.model = LogisticRegression(
                max_iter=model_params.n_iter, solver=model_params.solver
            ).fit(features, target)

        return self.model

    def predict(self, features: pd.DataFrame) -> np.ndarray:
        """
            make predictions
        """

        self.predicts = self.model.predict(features)
        return self.predicts

    def evaluate(self, predicts: np.ndarray, target: pd.Series) -> Dict[str, int]:
        """
            evaluate the predictions
        """

        metrics_dict = {}
        if "accuracy" in self.metric_params:
            metrics_dict.update({"accuracy": accuracy_score(target, predicts)})
        if "roc_auc" in self.metric_params:
            metrics_dict.update({"roc_auc": metrics.roc_auc_score(target, predicts)})
        if "f1" in self.metric_params:
            metrics_dict.update({"f1": metrics.f1_score(target, predicts)})
        return metrics_dict

    def serialize_model(self, output: str) -> str:
        """
            save model
        """
        with open(output, "wb") as file:
            pickle.dump(self.model, file)
        self.path = output
        return output

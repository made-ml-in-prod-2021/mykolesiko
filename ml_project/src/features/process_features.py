"""
    Transformer Class
"""
import numpy as np
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from src.config import FeatureParams
from sklearn.base import BaseEstimator, TransformerMixin


class TransformerClass (BaseEstimator, TransformerMixin):
    """
        TransformerClass
    """
    def __init__(self):
        pass

    def create_pipeline_for_categorical_params(self) -> Pipeline:
        """
            processing of categorical params
        """
        return Pipeline([("OH", OneHotEncoder())])

    def create_pipeline_for_numerical_params(self) -> Pipeline:
        """
                    processing of numerical params
        """
        return Pipeline([("impute", SimpleImputer(np.nan, "mean"))])

    def create(self, params: FeatureParams) -> ColumnTransformer:
        """
                create transformer pipeline
        """
        self.transformer = ColumnTransformer(
            [
                (
                    "pipeline_for_categorical_params",
                    self.create_pipeline_for_categorical_params(),
                    params.categorical,
                ),
                (
                    "pipeline_for_numerical_params",
                    self.create_pipeline_for_numerical_params(),
                    params.numerical,
                ),
            ]
        )
        return self.transformer

    def save(self, path_to_save: str) -> str:
        """
            save transformer to disk
        """
        with open(path_to_save, "wb") as file:
            pickle.dump(self.transformer, file)
        return path_to_save

    def load(self, path_to_save: str) -> ColumnTransformer:
        """
              load transformer from disk
        """
        with open(path_to_save, "rb") as file:
            self.transformer = pickle.load(file)
        return self.transformer

    def fit(self, df: pd.DataFrame, params: FeatureParams) -> pd.DataFrame:
        """
             fit the transformer to input data
        """
        self.create(params)
        self.transformer.fit(df)
        return self

    def fit_transform(self, df: pd.DataFrame, params: FeatureParams) -> pd.DataFrame:
        """
            fit the transformer to input data and transform the data
        """
        self.create(params)
        return pd.DataFrame(self.transformer.fit_transform(df))

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
            transform the data with already fitted transformer
        """
        return pd.DataFrame(self.transformer.transform(df))


def create_target(data: pd.DataFrame, params: FeatureParams) -> pd.Series:
    """
        extract target from data
    """
    return data[params.target]

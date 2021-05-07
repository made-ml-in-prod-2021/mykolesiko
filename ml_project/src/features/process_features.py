import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from src.config import FeatureParams
import pickle

class TransformerClass:
    def __init__(self):
        pass

    def create_pipeline_for_categorical_params(self) -> Pipeline:
        return Pipeline([("OH", OneHotEncoder())])

    def create_pipeline_for_numerical_params(self) -> Pipeline:
        return Pipeline([("impute", SimpleImputer(np.nan, "mean"))])

    def create(self, params: FeatureParams) -> ColumnTransformer:
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

    def save(self, path_to_save : str) -> str:
        with open(path_to_save, "wb") as f:
            pickle.dump(self.transformer, f)
        return path_to_save


    def load(self, path_to_save : str) -> ColumnTransformer:
        with open(path_to_save, "rb") as f:
            self.transformer = pickle.load(f)
        return self.transformer

    def fit_transform(self, df: pd.DataFrame, params: FeatureParams) -> pd.DataFrame:
        self.create(params)
        return pd.DataFrame(self.transformer.fit_transform(df))

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame(self.transformer.transform(df))



def create_target(data: pd.DataFrame, params: FeatureParams) -> pd.Series:
    return data[params.target]


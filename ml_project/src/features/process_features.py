import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from src.config import FeatureParams


def create_pipeline_for_categorical_params() -> Pipeline:
    return Pipeline(
        [
            ("OH", OneHotEncoder())
        ]
    )

def create_pipeline_for_numerical_params() -> Pipeline:
    return Pipeline(
        [
            ("impute", SimpleImputer(np.nan, 'mean'))
            
        ]
    )


def create_transformer(params: FeatureParams) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            ("pipeline_for_categorical_params",  create_pipeline_for_categorical_params(), 
            params.categorical),
            ("pipeline_for_numerical_params",  create_pipeline_for_numerical_params(), 
            params.numerical),
        ]
    )
    return transformer


def create_target(data: pd.DataFrame, params: FeatureParams) -> pd.Series:
    return data[params.target]


def create_feature_array(transformer: ColumnTransformer, df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(transformer.fit_transform(df))    
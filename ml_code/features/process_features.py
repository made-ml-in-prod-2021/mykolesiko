import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


create_pipeline_for_categorial_params() -> Pipeline:
    return(
        [
            ("OH", OneHotEncoder())
        ]
    )

create_pipeline_for_numerical_params() -> Pipeline:
    return(
        [
            ("impute", SimpleImputer(np.nan, 'mean'))
            
        ]
    )


def create_transformer(params: Features) -> ColumnsTransformer:
    transformer = ColumnsTransformer(
        [
            ("pipeline_for_categorial_params",  create_pipeline_for_categorial_params(), 
            params.categorial),
            #("pipeline_for_numerical_params",  create_pipeline_for_numerical_params(), 
            #params.numerical),
        ]
    )
    return transformer


def create_target(data: pd.DataFrame, params: FeatureParams) -> pd.Series:
    return data[params.target]
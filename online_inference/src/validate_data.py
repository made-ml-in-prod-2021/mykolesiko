from typing import List, Union

import numpy as np
from pydantic import BaseModel, conlist, validator

FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]

class PredictRequest(BaseModel):
    data: List[conlist(Union[float, str], min_items=1, max_items=16)]
    features: List[str]

    @validator("features")
    def check_features(cls, features):
        if not features == FEATURES:
            raise ValueError(
                f"Check features: Proper features are {FEATURES}"
            )
        return features
    @validator("data")
    def check_data(cls, data):
        if np.array(data).shape[1] != len(FEATURES):
            raise ValueError(
                f"Proper count of columns in data is : {len(FEATURES)}"
            )
        return data


class PredictResponse(BaseModel):
    #id: str
    diagnosis: str

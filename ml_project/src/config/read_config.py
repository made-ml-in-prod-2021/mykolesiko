"""
    Yaml configuration
"""

from dataclasses import dataclass, field
from typing import List, Optional, Any
from marshmallow_dataclass import class_schema
import yaml



@dataclass()
class ModelParams:
    """
        Params of model
    """
    model_type: str
    n_estimators: Optional[int] = 100
    n_iter: Optional[int] = 100
    solver: Optional[str] = "liblinear"


@dataclass()
class FeatureParams:
    """
            Feature Params
        """
    categorical: List[str]
    numerical: List[str]
    target: Optional[str]


@dataclass()
class SplittingParams:
    """
            Params of splitting data
    """
    val_size: float
    random_state: Optional[int] = None
    stratify: Optional[str] = None
    shuffle: Optional[bool] = True


@dataclass()
class TransformerParams:
    """
                Params of transformer
    """
    file: str


@dataclass()
class TrainingConfigParams:
    """
        Params of all yaml configuration
    """
    model_folder: str
    input_data_file: str
    model_file: str
    metric_file: str
    splitting_params: SplittingParams
    model_params: ModelParams
    metric_params: List[str]
    feature_params: FeatureParams
    transformer_params: TransformerParams
    logging_config: str


ConfigSchema = class_schema(TrainingConfigParams)


def read_training_config_params(path: str) -> TrainingConfigParams:
    """
        reading data from yaml
    """
    with open(path, "r") as config:
        schema = ConfigSchema()
        return schema.load(yaml.safe_load(config))

from marshmallow_dataclass import class_schema
import yaml

from dataclasses import dataclass, field
from typing import List, Optional, Any


@dataclass()
class ModelParams:
    model_type: str


@dataclass()
class FeatureParams:
    categorical: List[str]
    numerical: List[str]
    target: Optional[str]


@dataclass()
class SplittingParams:
    val_size: float
    random_state: int
    stratify: Optional[str] = None


@dataclass()
class TransformerParams:
    file: str


@dataclass()
class TrainingConfigParams:
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
    with open(path, "r") as config:
        schema = ConfigSchema()
        return schema.load(yaml.safe_load(config))

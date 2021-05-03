from dataclasses import dataclass
from .split_params import SplittingParams
from .feature_params import FeatureParams
from .train_params import TrainingParams
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class TrainingConfigParams:
    input_data_path: str
    output_model_path: str
    metric_path: str
    splitting_params: SplittingParams
    feature_params: FeatureParams
    model_params: ModelParams
    


ConfigSchema = class_schema(TrainingConfigParams)


def read_training_config_params(path: str) -> TrainingPipelineParams:
    with open(path, "r") as config:
        schema = ConfigSchema()
        return schema.load(yaml.safe_load(config))
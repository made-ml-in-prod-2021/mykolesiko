from marshmallow_dataclass import class_schema
import yaml

from dataclasses import dataclass, field
from typing import List, Optional, Any



# @dataclass()
# class ModelParams:
#     model_type: str
#
#
# @dataclass()
# class FeatureParams:
#     categorical: List[str]
#     numerical: List[str]
#     target: Optional[str]
#
#
# @dataclass()
# class SplittingParams:
#     val_size: float
#     random_state: int
#     stratify: Optional[str] = None
#
#
# @dataclass()
# class TransformerParams:
#     path: str
#
# @dataclass()
# class TrainingConfigParams:
#     name : str
#     input_data_path: str
#     output_model_path: str
#     metric_path: str
#     splitting_params: SplittingParams
#     model_params: ModelParams
#     metric_params: List[str]
#     feature_params: FeatureParams
#     transformer_params:  TransformerParams


#ConfigSchema = class_schema(TrainingConfigParams)


def test_read_training_config_params(test_config_yaml : str)
    with open(test_config_yaml, "r") as config:
        schema = ConfigSchema()
        params = schema.load(yaml.safe_load(config))
        print(params)
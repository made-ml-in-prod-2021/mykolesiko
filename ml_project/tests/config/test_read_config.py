from marshmallow_dataclass import class_schema
import yaml

from dataclasses import dataclass, field
from typing import List, Optional, Any
import pytest
from src.config import (
    TrainingConfigParams,
    SplittingParams,
    FeatureParams,
    ModelParams,
    TransformerParams,
    read_training_config_params,
)


# model_folder : "test"
# input_data_file: "heart.csv"
# model_file: "model.pkl"
# metric_file: "metrics.json"
# splitting_params:
#   val_size: 0.3
#   random_state: 32
#   stratify:
# model_params:
#   model_type: "LogisticRegression"
# metric_params:
#     - "accuracy"
#     - "roc_auc"
# feature_params:
#   categorical:
#     - "sex"
#     - "cp"
#     - "fbs"
#     - "exang"
#     - "slope"
#     - "ca"
#     - "thal"
#   numerical:
#     - "age"
#     - "trestbps"
#     - "chol"
#     - "restecg"
#     - "thalach"
#     - "oldpeak"
#   target: "target"
# transformer_params:
#   file:  "transformer.pkl"
# logging_config: "logging_default.yaml"


@pytest.mark.parametrize(
    "yaml_params",
    [
        pytest.param(
            TrainingConfigParams(
                "test",
                "heart.csv",
                "model.pkl",
                "metrics.json",
                SplittingParams(0.3, 32, None),
                ModelParams("LogisticRegression"),
                ["accuracy", "roc_auc"],
                FeatureParams(
                    ["sex", "cp", "fbs", "exang", "slope", "ca", "thal"],
                    ["age", "trestbps", "chol", "restecg", "thalach", "oldpeak"],
                    "target"
                ),
                TransformerParams("transformer.pkl"),
                "logging_default.yaml",
            )
        )
    ],
)
def test_read_training_config_params(test_config_yaml: str, yaml_params: TrainingConfigParams, logger):
    logger.info(f"test_read_training_config_params")
    params = read_training_config_params(test_config_yaml)
    logger.info(f"config = {params}")
    assert params == yaml_params

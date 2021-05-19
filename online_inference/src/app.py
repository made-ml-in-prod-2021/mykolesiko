import logging
import os
import pickle
from typing import List, Union, Optional

import numpy as np
import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, conlist
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from src.validate_data import PredictResponse, PredictRequest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

TRANSFORMER_PATH = "models/transformer.pkl"
MODEL_PATH = "models/model.pkl"

def int_to_diagnose(target: int) -> str:
   if (target == 1):
        return ("Sick")
   else:
        return ("Health")

def load_object(path: str) -> Pipeline:
    with open(path, "rb") as f:
        logger.info(f"load model from path: {path}")
        return pickle.load(f)

model: Optional[Pipeline] = None

def make_predict(data: List, features: List[str], model: Pipeline) -> List[PredictResponse]:

    data = pd.DataFrame(data, columns=features)
    #ids = map(int(data["id"].tolist()))

    logger.info(f"load model: {model}")
    model = load_object(MODEL_PATH)
    logger.info(f"load model: {model}")
    transformer = load_object(TRANSFORMER_PATH)
    logger.info(f"load transformer: {transformer}")
    data_processed = transformer.transform(data)
    predictions = model.predict(data_processed)
    predictions_str = list(map(int_to_diagnose,predictions))
    return [
         PredictResponse(diagnosis=prediction) for  prediction in  predictions_str
    ]


app = FastAPI()


@app.get("/")
def main():
    return "it is entry point of our predictor"


@app.on_event("startup")
def load_model():
    global model
    model_path = MODEL_PATH
    if model_path is None:
        err = f"PATH_TO_MODEL {model_path} is None"
        logger.error(err)
        raise RuntimeError(err)

    model = load_object(model_path)


@app.get("/health")
def health() -> bool:
    return not (model is None)


@app.get("/predict/", response_model=List[PredictResponse])
def predict(request: PredictRequest):
    return make_predict(request.data, request.features, model)


if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))

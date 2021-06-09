import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score
import click
import os
import numpy as np
from typing import Dict
import json



def load_model(path : str):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def evaluate(predicts: np.ndarray, target: pd.Series) -> Dict[str, int]:
        """
            evaluate the predictions
        """

        metrics_dict = {}
        metrics_dict.update({"accuracy": accuracy_score(target, predicts)})
        metrics_dict.update({"roc_auc": roc_auc_score(target, predicts)})
        metrics_dict.update({"f1": f1_score(target, predicts)})
        return metrics_dict




@click.command("validate")
@click.option("--input-dir")
@click.option("--model-dir")
#@click.option("--output-dir")
def validate(input_dir: str, model_dir: str):
    val_data = pd.read_csv(os.path.join(input_dir, "val_data.csv"))
    val_target = pd.read_csv(os.path.join(input_dir, "val_target.csv"))

    model = load_model(os.path.join(model_dir, "model.pkl"))
    val_predict = model.predict(val_data)
    val_real = val_target['target'].tolist() 	
    metrics = evaluate(val_predict, val_real)
    
	
    with open(os.path.join(model_dir, "metrics.json"), "w") as metric_file:
        json.dump(metrics, metric_file)


    #os.makedirs(output_dir, exist_ok=True)
    #save_model(model, output_dir)


if __name__ == '__main__':
    validate()
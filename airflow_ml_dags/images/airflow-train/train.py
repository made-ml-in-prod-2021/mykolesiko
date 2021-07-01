from typing import Tuple
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import click
import os


N_ESTIMATORS = 300


def save_model(model, output_dir : str) -> None:
   with open(os.path.join(output_dir, "model.pkl"), "wb") as f:
        pickle.dump(model, f)



@click.command("train")
@click.option("--input-dir")
@click.option("--output-dir")
def train(input_dir: str, output_dir):
    train_data = pd.read_csv(os.path.join(input_dir, "train_data.csv"))
    train_target = pd.read_csv(os.path.join(input_dir, "train_target.csv"))

    model = RandomForestClassifier(N_ESTIMATORS).fit(train_data, train_target['target'].tolist())

    os.makedirs(output_dir, exist_ok=True)
    save_model(model, output_dir)


if __name__ == '__main__':
    train()
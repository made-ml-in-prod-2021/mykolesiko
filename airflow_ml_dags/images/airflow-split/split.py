from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
import click
import os

SPLIT = 0.2


def split_train_val_data(data: pd.DataFrame, target: pd.Series) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    :rtype: object
    """

    train_data, val_data, y_train, y_test = train_test_split(
        data,
        target,
        train_size=None,
        test_size=SPLIT,
        random_state=True,
        shuffle=True,
        stratify=None,
    )
    return train_data, val_data, y_train, y_test


@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
def split(input_dir: str, output_dir):
    data = pd.read_csv(os.path.join(input_dir, "data_processed.csv"))
    target = pd.read_csv(os.path.join(input_dir, "target.csv"))

    train_data, val_data, y_train, y_test = split_train_val_data(data, target)
    os.makedirs(output_dir, exist_ok=True)
    train_data.to_csv(os.path.join(output_dir, "train_data.csv"), index = None)
    val_data.to_csv(os.path.join(output_dir, "val_data.csv") , index = None)
    y_train.to_csv(os.path.join(output_dir, "train_target.csv"), index = None)
    y_test.to_csv(os.path.join(output_dir, "val_target.csv"), index = None)


if __name__ == '__main__':
    split()
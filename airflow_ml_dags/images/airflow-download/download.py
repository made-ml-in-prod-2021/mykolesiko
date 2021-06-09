import os
import click
from collections import Counter
import random
import pandas as pd
import numpy as np
from typing import Tuple


NUM_ROWS = 100

def generate_from_hist(list_col: list, num_rows: int) -> list:
    """
        generate data based on distribution of column
    """
    list_col_unique = list(set(list_col))
    cnt = Counter(list_col)
    freq = [cnt[value] for value in list_col_unique]
    list_col_new = random.choices(list_col_unique, weights=freq, k=num_rows)
    return list_col_new



def generate_data(path_to_train_csv: str, num_rows: int, path_to_generated_data: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
            generate data for tests
    """

    data_first = pd.read_csv(path_to_train_csv)
    data = data_first.drop(columns=["target"])
    data_new = pd.DataFrame(columns=data.columns)
    for col in data.columns:
        list_col = data[col].to_list()
        list_col_new = generate_from_hist(list_col, int(num_rows))
        data_new[col] = list_col_new
    #data_new[data.columns].to_csv(path_to_generated_data, index=False)
    target = pd.DataFrame(columns = ['target'])
    target['target'] = np.random.binomial(n=1, p=0.7, size=NUM_ROWS).astype(int)
    return data_new, target


@click.command('download')
@click.option('--train_dir', required=True)
@click.option('--output_dir', required=True)
def download(train_dir: str, output_dir : str) -> None:

    data, target = generate_data(os.path.join(train_dir, "heart.csv"), NUM_ROWS, output_dir)
    test_data, test_target = generate_data(os.path.join(train_dir, "heart.csv"), NUM_ROWS, output_dir)

    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, 'data.csv'), index=False)
    target.to_csv(os.path.join(output_dir, 'target.csv'), index=False)
    test_data.to_csv(os.path.join(output_dir, 'test_data.csv'), index=False)
    test_target.to_csv(os.path.join(output_dir, 'test_target.csv'), index=False)


if __name__ == '__main__':
    download()

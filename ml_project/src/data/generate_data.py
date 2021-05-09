from collections import Counter
#import numpy as np
import random
import pandas as pd


def generate_from_hist(list_col: list, num_rows: int) -> list:
    """
        generate data based on distribution of column
    """

    list_col_unique = list(set(list_col))
    cnt = Counter(list_col)
    freq = [cnt[value] for value in list_col_unique]
    # print(freq)
    list_col_new = random.choices(list_col_unique, weights=freq, k=num_rows)
    return list_col_new
    # probs = freq/freq.sum()


def generate_data(path_to_train_csv: str, num_rows: int, path_to_generated_data: str) -> pd.DataFrame:
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
    data_new[data.columns].to_csv(path_to_generated_data, index=False)
    # print(data_new.head())

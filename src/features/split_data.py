from typing import Tuple
from sklearn.model_selection import train_test_split

def split_train_val_data(
    data: pd.DataFrame, target : pd.Series, params: SplittingParams
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    :rtype: object
    """
    stratify = None
    if params.stratify is not None:
      stratify = target
    train_data, val_data, y_train, y_test = train_test_split(
        data, target, test_size=params.val_size, random_state=params.random_state, shuffle = True, stratify = stratify
    )
    return train_data, val_data, y_train, y_test
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass()
class FeatureParams:
    categ_cols: List[str]
    numerical_cols: List[str]
    target_col: Optional[str]
    
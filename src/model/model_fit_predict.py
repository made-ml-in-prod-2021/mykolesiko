from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from typing import Dict, Union

ModelType = Union[RandomForestClassifier, LogisticRegression]

class ModelClass:
    def __init__(self, params : ModelParams):
        self.params = params
        
       
    def train(self, features: pd.DataFrame, target: pd.Series) -> ModelType:
        print(self.params.model_type)
        if self.params.model_type == "RandomForestClassifier":
            self.model = RandomForestClassifier(
                n_estimators=600, 
            ).fit(features, target)
        elif self.params.model_type == "GradientBoostingClassifier":
            self.model = GradientBoostingClassifier(n_estimators=100).fit(features, target)
        else:
            self.model = LogisticRegression(max_iter=1000).fit(features, target)
        
        return self.model

    def predict(self, features: pd.DataFrame) -> np.ndarray:
        predicts = self.model.predict(features)
        return predicts

    def evaluate(self, predicts: np.ndarray, target: pd.Series) -> Dict[str, int] :
        return {
            "accuracy": accuracy_score(target, predicts)
        }
        #"rmse": mean_squared_error(target, predicts, squared=False),
        #"mae": mean_absolute_error(target, predicts),
    
    def serialize_model(self, output: str) -> str:
        with open(output, "wb") as f:
            pickle.dump(self.model, f)
        return output


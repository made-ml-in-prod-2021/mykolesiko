import os
import pandas as pd
import click
import pickle


def load_model(path : str):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model



@click.command("predict")
@click.option("--input-dir")
@click.option("--model-dir")
@click.option("--output-dir")
def predict(input_dir: str, model_dir : str, output_dir: str):
    test_data = pd.read_csv(os.path.join(input_dir, "test_data.csv"))

    model = load_model(os.path.join(model_dir, "model.pkl"))
    test_predict = pd.DataFrame(model.predict(test_data), columns = ['target'])

    os.makedirs(output_dir, exist_ok=True)
    	
    test_predict.to_csv(os.path.join(output_dir, "test_predict.csv"), index = None)


if __name__ == '__main__':
    predict()
import os
import pandas as pd
import click

from sklearn.preprocessing import StandardScaler 




@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess(input_dir: str, output_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    target = pd.read_csv(os.path.join(input_dir, "target.csv"))

    scaler = StandardScaler() 	
    data_processed = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)	
    os.makedirs(output_dir, exist_ok=True)
    data_processed.to_csv(os.path.join(output_dir, "data_processed.csv"), index = None)
    target.to_csv(os.path.join(output_dir, "target.csv"), index = None)


if __name__ == '__main__':
    preprocess()
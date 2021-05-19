import numpy as np
import pandas as pd
import requests
import click



@click.command()
@click.option("--host", default="localhost")
@click.option("--port", default=8000)
@click.option("--path_to_data", default="./heart.csv")
@click.option("--num_predictions", default=100)
def predict(host, port, path_to_data, num_predictions):
    data = pd.read_csv(path_to_data)
    request_features = list(data.columns)
    print(request_features)
    for i in range(num_predictions):
        request_data = [x for x in data.iloc[i].tolist()]
        print(request_data)
        response = requests.get(
            f"http://{host}:{port}/predict/",
            json={"data": [request_data], "features": request_features},
        )
        print(response.status_code)
        print(response.json())


if __name__ == "__main__":	
	predict()
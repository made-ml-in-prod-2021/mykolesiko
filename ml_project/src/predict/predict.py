from src.model_fit_predict import ModelClass


def setup_parser(parser):
    """Setups parser"""
    # parser.set_defaults(callback=callback_analytics)

    parser.add_argument(
        "--data_path", "-dp",
        required=True,
        default=None,
        help="path to data",
        metavar="FPATH",
    )

    parser.add_argument(
        "--model_path", "-mp",
        required=True,
        default=None,
        help="path to model",
        metavar="FPATH",
    )
    parser.add_argument(
        "--save_path", "-sp",
        required=True,
        default=None,
        help="path to saved predictions",
        metavar="FPATH",
    )


def predict(data_path: str, model_path: str, save_path: str, params: FeatureParams):
    logger.info(f"start predict data from {data_path}, model from {model_path}")
    model = ModelClass()
    sklearn_model = model.load(model_path)
    logger.info(f"load model: {sklearn_model}")
    data = pd.read_csv(data_path)
    logger.info(f"read data shape: {data.shape}")

    logger.info(f"transform the features {params}")
    transformer = load_transformer(model_path)
    data_processed = create_feature_array(transformer, data)
    prediction = model.predict(data)
    pd.DataFrame(predictions).to_csv(f"{save_path}")
    return prediction


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="load data and model and make predict",
        description="instrument for making prediction",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    setup_logging(arguments.logs)
    # arguments.callback(arguments)

    predictions = predict(data_path: str, model_path: str, save_path: str, params: FeatureParams):
    #print(metrics)



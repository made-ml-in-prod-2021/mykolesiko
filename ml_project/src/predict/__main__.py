"""
    main module for prediction util
"""

import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from src.logs import setup_logging
from src.logs import LOGGER_YAML_DEFAULT
from .predict import predict



def setup_parser(parser):
    """Setups parser"""
    # parser.set_defaults(callback=callback_analytics)

    parser.add_argument(
        "--data",
        "-dp",
        required=True,
        default=None,
        help="path to data",
        metavar="FPATH",
    )

    parser.add_argument(
        "--config",
        "-c",
        required=True,
        default=None,
        help="path to config model file",
        metavar="FPATH",
    )


    parser.add_argument(
        "--model",
        "-mp",
        required=True,
        default=None,
        help="path to model",
        metavar="FPATH",
    )

    parser.add_argument(
        "--transformer",
        "-tp",
        required=True,
        default=None,
        help="path to transformer",
        metavar="FPATH",
    )

    parser.add_argument(
        "--output",
        "-sp",
        required=True,
        default=None,
        help="path to saved predictions",
        metavar="FPATH",
    )


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="load data and model and make predict",
        description="instrument for making prediction",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    setup_parser(parser)
    arguments = parser.parse_args()
    if not os.path.exists(arguments.output):
        os.mkdir(arguments.output)

    setup_logging(LOGGER_YAML_DEFAULT, os.path.join(arguments.output, "predict.log"))
    # arguments.callback(arguments)

    predictions = predict(
        arguments.data, arguments.config, arguments.model, arguments.transformer, arguments.output
    )


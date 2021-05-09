"""
    main for util generate data for tests and for predictions
"""
#import logging
#import os
#import pickle
#import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
#from src.constants import CONFIG_DIR
from .generate_data import generate_data


def setup_parser(parser):
    """Setups parser"""
    # parser.set_defaults(callback=callback_analytics)

    parser.add_argument(
        "--train_data",
        required=True,
        default=None,
        help="path to input data (csv), which would be taken for data generation",
        metavar="FPATH",
    )

    parser.add_argument(
        "--rows",
        required=True,
        default=None,
        help="number of rows to generate",
        metavar="FPATH",
    )

    parser.add_argument(
        "--test_data",
        required=True,
        default=None,
        help="path to generated data (csv)",
        metavar="FPATH",
    )


if __name__ == "__main__":
    # print("1")
    parser = ArgumentParser(
        prog="generator of data using train data",
        description="instrument for generating data to test",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    setup_parser(parser)
    arguments = parser.parse_args()
    # print(arguments)
    generate_data(arguments.train_data, arguments.rows, arguments.test_data)

# pylint: disable = missing-module-docstring, missing-class-docstring, missing-function-docstring
import argparse
from json_journal.cli import balance


def cli():
    top_level_parser = argparse.ArgumentParser()

    subparsers = top_level_parser.add_subparsers()
    balance.builder(subparsers)

    args = top_level_parser.parse_args()
    args.handler(args)

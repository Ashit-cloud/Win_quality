## read params
## process
## return dataframe
import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config= yaml_file.safe_load(yaml)
    return config


def get_data(config_path):
    config = read_params(config_path)
    print(config)


if __name__ =="__mian__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path = parsed_args.config)
    
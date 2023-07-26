from argparse import ArgumentParser
import os
import pickle

import pandas as pd
from speakleash import Speakleash, Reader

def parse_args():
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("--project_name", "-p", help="Input project name from speakleash dataset", required=True, type=str)
    args = parser.parse_args()
    return args

def get_reader(project_name: str, speakleash_class: Speakleash) -> Reader.stream_data:
    return speakleash_class.get(project_name).ext_data

def get_dataframe(project_name: str, speakleash_class: Speakleash) -> pd.DataFrame:
    reader = get_reader(project_name, speakleash_class)
    return pd.DataFrame({"text": s[0]} | s[1] for s in reader)

if __name__ == '__main__':

    # defining project name
    PROJECT = parse_args().project_name

    # initiating directory
    base_dir = os.path.join('datasets')
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # initiating Speakleash
    sl = Speakleash(base_dir)

    # creating dataframe
    df = get_dataframe(PROJECT, sl)

    # <optional> saving dataframe as pickle
    with open(f"{base_dir}/{PROJECT}.pkl","wb") as f:
        pickle.dump(df, f)

# Get a dataframe from a SpeakLeash project

import os
import pandas as pd
import pickle


from speakleash import Speakleash, Reader


def get_reader(project_name: str, speakleash_class: Speakleash) -> Reader.stream_data:
    return speakleash_class.get(project_name).ext_data


def get_dataframe(project_name: str, speakleash_class: Speakleash) -> pd.DataFrame:
    reader = get_reader(project_name, speakleash_class)
    return pd.DataFrame({"text": s[0]} | s[1] for s in reader)


if __name__ == '__main__':
    PROJECT = input('Enter a dataset name: ')

    # Initiating directory
    base_dir = os.path.join('datasets')
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Initiating Speakleash
    sl = Speakleash(base_dir)

    # Creating dataframe
    df = get_dataframe(PROJECT, sl)

    # <optional> Saving dataframe as pickle
    with open(f"{base_dir}/{PROJECT}.pkl", "wb") as f:
        pickle.dump(df, f)

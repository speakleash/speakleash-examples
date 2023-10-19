"""Import SpeakLeash dataset into a pandas / polars dataframe."""

import os
import gc

from speakleash import Speakleash
import pandas as pd
import polars


if __name__ == '__main__':
    
    # Select dataset - "thesis" is small dataset but with "plwiki" memory usage is: 
    # pandas dataframe ~ 4.2GB (RAM usage peak ~ 10GiB)
    # polars dataframe ~ 2.3GB (RAM usage peak ~ 6GiB)
    PROJECT = "thesis"

    # Initiating directory
    base_dir = os.path.join('datasets')
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Initiating Speakleash
    sl = Speakleash(base_dir)

    # Get data
    data = sl.get(PROJECT).ext_data

    # Creating pandas DataFrame
    print("--- Pandas DataFrame ---")
    pandas_df = pd.DataFrame({"text": s[0], **s[1]} for s in data)
    print(pandas_df.info(memory_usage='deep'))

    # Delete variables to free memory 
    del data
    del pandas_df
    gc.collect()

    # Get data
    data = sl.get(PROJECT).ext_data

    # Creating polars DataFrame
    print("--- Polars DataFrame ---")
    polars_df = polars.DataFrame({"text": s[0], **s[1]} for s in data)
    print(polars_df.schema)
    print(polars_df.shape)
    mem_size = polars_df.estimated_size("mb")
    print(f"Polars memory usage: {mem_size:.2f} MB = {(mem_size / 1000):.2f} GB")

    del data
    del polars_df
    gc.collect()

    # <optional> Saving dataframe as pickle
    # pandas_df.to_pickle(f"{PROJECT}.pkl")
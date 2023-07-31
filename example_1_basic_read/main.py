"""Speakleash: basic read of metadata and documents"""

import os

from speakleash import Speakleash


if __name__ == '__main__':

    base_dir = os.path.join(".")
    replicate_to = os.path.join(base_dir, "datasets")
    print(f"Replicate datasets to: {replicate_to}")
    sl = Speakleash(replicate_to)

    # Iterate over Speakleash datasets
    for ds in sl.datasets:
        print(ds.name)

        # Import dataset and iterate through documents
        for doc in ds.ext_data:
            txt, meta = doc
            print(f"Metadata: \n{meta}\n")
            print(f"Docs: \n{txt[:500]}[...]\n")
            break
        break

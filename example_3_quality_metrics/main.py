"""Speakleash: get dataset quality metrics"""

import os

from speakleash import Speakleash


if __name__ == '__main__':

    base_dir = os.path.join(".")
    replicate_to = os.path.join(base_dir, "datasets")
    print(f"Replicate datasets to: {replicate_to}")
    sl = Speakleash(replicate_to)

    # Choose dataset
    dataset_name = "web_artykuły_finanse_3"

    # Import quality metrics distribution for selected dataset
    if sl.get(dataset_name).quality_metrics:
        print(f"Quality metrics: {sl.get(dataset_name).quality} \n")

    # Import dataset (documents and their metadata)
    ds = sl.get(dataset_name).ext_data
    limit = 5

    # Iterate over documents in dataset
    for index, doc in enumerate(ds):

        txt, meta = doc
        doc_quality = meta.get("quality", "")

        # Check quality metrics
        if doc_quality == 'HIGH':
            print("~ High-quality document:")
        elif doc_quality == 'MEDIUM':
            print("~ Medium-quality document:")
        elif doc_quality == 'LOW':
            print("~ Low-quality document:")

        # Print part of document
        print(txt[:150] + f' [... + more {len(txt)-150} characters] \n')

        if index == limit-1:
            break

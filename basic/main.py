from speakleash import Speakleash
import os

base_dir = os.path.join(".")
replicate_to = os.path.join(base_dir, "datasets")
sl = Speakleash(replicate_to)

for ds in sl.datasets:
    print(ds.name)
    for doc in ds.ext_data:
        txt, meta = doc
        print(txt)
        break
    break


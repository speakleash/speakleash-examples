from speakleash import Speakleash
import os

base_dir = os.path.join(".")
replicate_to = os.path.join(base_dir, "datasets")

sl = Speakleash(replicate_to)
name = "web_artykuły_finanse_3"

print("Replicate to:", replicate_to)

if sl.get(name).quality_metrics:
    print(sl.get(name).quality)

limit = 5
counter = 0
ds = sl.get(name).ext_data

for doc in ds:

    txt, meta = doc

    if meta.get("quality", "") == 'HIGH':
        print("High-quality document")

    if meta.get("quality", "") == 'LOW':
        print("Low-quality document")

    if meta.get("quality", "") == 'MEDIUM':
        print("Medium-quality document")

    counter = counter + 1
    if counter > limit:
        break

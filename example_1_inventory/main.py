"""Speakleash datasets inventory"""
import os

from speakleash import Speakleash
from termcolor import colored

base_dir = os.path.join(".")
replicate_to = os.path.join(base_dir, "datasets")

sl = Speakleash(replicate_to)

print("name;size;extraction type;copyrigth label;license;license url")
  
for d in sl.datasets:
    
    manifest = d.manifest
    
    #Identification of extraction type
    extraction_type = manifest.get("type", "")
    formatted_extraction_type = colored("n/a", 'red')

    if extraction_type == "speakleash_crawls":
        formatted_extraction_type = colored("scraped", 'yellow')

    if extraction_type == "external_dataset":
        formatted_extraction_type = colored("external dataset", 'blue')

    #Size of dataset
    size_mb = round(d.characters/1024/1024)

    #Identification of the copyright description method
    copyrigth_label = colored("OLD", 'red')
    disclaimer  = manifest.get("disclaimer", "")

    if extraction_type == "speakleash_crawls":
        if len(disclaimer) > 0:
            copyrigth_label = colored("NEWEST", 'blue')
        else:
            copyrigth_label = colored("OLD", 'red')
    else:
        copyrigth_label = colored("standard", 'green')

    sources = manifest.get("sources", [])

    if len(sources) == 1:
        licence = sources[0].get("license", colored("n/a", 'red')).replace("/n", "").replace(";",",").strip()
        license_url = sources[0].get("license_url", "n/a")
    else:
        licence = "multiple"
        license_url = "n/a"

    print("{0};{1} MB;{2};{3};{4};{5}".format(colored(d.name,'green'), size_mb, formatted_extraction_type, copyrigth_label, licence, license_url))


"""Speakleash: datasets inventory check - table"""

import os

from speakleash import Speakleash
from termcolor import colored
from prettytable import PrettyTable


if __name__ == '__main__':

    base_dir = os.path.join(".")
    replicate_to = os.path.join(base_dir, "datasets")
    print("\nCollecting information from SpeakLeash database...\n")
    sl = Speakleash(replicate_to)

    # Create Pretty Table and set columns names
    inventory_table = PrettyTable()
    inventory_table.field_names = ["dataset name", "size [MB]", "extraction type",
                                    "copyrigth label", "license", "license_url"]

    for d in sl.datasets:
        # Extract manifest for each dataset
        manifest = d.manifest

        # Identification of extraction type
        extraction_type = manifest.get("type", "")
        formatted_extraction_type = colored("n/a", "red")

        if extraction_type == "speakleash_crawls":
            formatted_extraction_type = colored("scraped", "yellow")

        if extraction_type == "external_dataset":
            formatted_extraction_type = colored("external dataset", "blue")

        # Size of dataset
        size_mb = round(d.characters / 1024 / 1024)

        # Identification of the copyright description method
        copyrigth_label = colored("OLD", "red")
        disclaimer = manifest.get("disclaimer", "")

        if extraction_type == "speakleash_crawls":
            if len(disclaimer) > 0:
                copyrigth_label = colored("NEWEST", "blue")
            else:
                copyrigth_label = colored("OLD", "red")
        else:
            copyrigth_label = colored("standard", "green")

        # Identification of the license and license url
        sources = manifest.get("sources", [])
        if len(sources) == 1:
            licence = (sources[0].get("license", colored("n/a", "red"))
                        .replace("/n", "").replace(";", ",").strip())
            license_url = sources[0].get("license_url", "n/a")
        else:
            licence = "multiple"
            license_url = "n/a"

        # Add row to Pretty Table with dataset information
        inventory_table.add_row([colored(d.name, "green"), f"{size_mb:,}".replace(",", " "),
                                 formatted_extraction_type, copyrigth_label,
                                 licence[:30], license_url[:30],])


    inventory_table.align["size [MB]"] = "r"
    print(inventory_table)

# README.md

## Synopsis

Example shows how to extract high quality documents from selected dataset. \
This Python module provides functionalities to create necessary directories and save documents of specified quality from the speakleash dataset to a specific folder location.

## Features

- Creates required directories if they do not exist.
- Saves documents of specified quality from the `speakleash` dataset to a specified folder.

## Dependencies

- `os`
- `speakleash`

## Setup

In the script, there are two configurable parameters — name and limit.

- `name` is the dataset name from which high-quality documents will be fetched
- `limit` defines the number of documents to be retrieved from the selected dataset

You'll find these settings in the config section of the script:
```
# CONFIG
name = "plwiki"  # provide dataset name from where will be taken HIGH quality documents
limit = 10  # write how many files you want to collect from selected dataset
```

## Installation

Make sure to have `speakleash` package installed.

## Usage

1. Use the `get_data(txt_folder_name)` function to create directories where `txt_folder_name` is the name of the folder where the high-quality documents will be saved.
2. Use the `save_quality_docs(txt_folder_name, quality)` function for saving documents of a given quality where `quality` is the quality of data to be downloaded and saved.

### Example
The script could be used as follows:

```
txt_folder_name = "datasets_high_quality_txt"
get_data(txt_folder_name)
save_quality_docs(txt_folder_name, "HIGH")
```

The script can be imported, and the functions get_data and save_quality_docs can be used in other Python scripts.

### Output

The script will create a folder named "datasets" in its directory to store the downloaded dataset. Further, a folder named txt_folder_name as specified by the user will be created to store high-quality text files.
If the folders are already present, the script will not create them again. Instead, it will capture data as per the instructions and save it to the specified location.


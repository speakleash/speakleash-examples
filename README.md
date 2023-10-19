# Speakleash-examples

Sample codes on how to use [SpeakLeash](https://github.com/speakleash/speakleash) python package:

## Basics

[example_1_basic_read](https://github.com/speakleash/speakleash-examples/tree/main/example_1_basic_read) <-- Script demonstrates how to iterate over datasets and documents in a given repository, printing the name of each dataset, as well as the metadata and text of each document.

[example_2_inventory_check](https://github.com/speakleash/speakleash-examples/tree/main/example_2_inventory_check) <-- Sample code demonstrates how to extract information about datasets from the Speakleash repository and print a summary of the metadata in a tabular format, with colorized fields for easier visibility. <br/>
<sup>(Additional libraries can be installed via _requirements.txt_ in this folder)</sup>

[example_3_quality_metrics](https://github.com/speakleash/speakleash-examples/tree/main/example_3_quality_metrics) <-- Example shows how to check quality metrics distribution in a given dataset and extract quality info for each document.

[example_4_extraction_to_files](https://github.com/speakleash/speakleash-examples/tree/main/example_4_extraction_to_files) <-- Example shows how to extract high quality documents from selected dataset and provides functionalities to create necessary directories and save documents of specified quality from the speakleash dataset to a specific folder location.

[example_5_word_cloud](https://github.com/speakleash/speakleash-examples/tree/main/example_5_word_cloud) <-- Example shows two cases of generation word cloud examples. The first case is with the usage of spaCy library, using the lemmatizer. Second case uses NLTK library.

[example_6_pandas](https://github.com/speakleash/speakleash-examples/tree/main/example_6_pandas) <-- Example shows how to put Speakleash dataset into the pandas DataFrame.

[example_7_pandas_polars](https://github.com/speakleash/speakleash-examples/tree/main/example_7_pandas_polars) <-- Example shows how to import data from SpeakLeash datasets into Pandas and Polars libraries dataframes.

[example_8_dataset_vis](https://github.com/speakleash/speakleash-examples/tree/main/example_8_dataset_vis) <-- Example shows how to load data from the SpeakLeash library datasets and visualize selected metrics considering document quality, among other things.
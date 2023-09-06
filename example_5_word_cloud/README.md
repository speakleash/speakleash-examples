# Example No. 4

There are 2 examples of Word Cloud creation in this folder:
- *main_1_spacy.py* - an example using the spaCy library, using the lemmatizer. To avoid the RAM usage problem, the processed documents are limited to a set number of characters.
- *main_2_nltk.py* - example using the NLTK library. The script is faster than the version using spaCy, but takes into account most words (excluding Polish stopwords).
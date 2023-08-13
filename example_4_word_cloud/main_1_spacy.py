"""Speakleash: basic wordcloud (using spacy)"""

import os
from collections import Counter

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from speakleash import Speakleash
import spacy



if __name__ == '__main__':

    PROJECT = 'form_symfonik'
    # If the documents in the dataset are too large, 
    # too much RAM may be allocated (spacy calculations), 
    # this may cause problems with the operation of the system.

    base_dir = os.path.join(os.path.dirname(__file__))
    replicate_to = os.path.join(base_dir, "datasets")

    sl = Speakleash(replicate_to)
    ds = sl.get(PROJECT).data

    wc = WordCloud()

    nlp = spacy.load('pl_core_news_md', disable=["ner", "parser", "tagger", "textcat"])
    nlp.max_length = 200000

    counts_all = Counter()
    limit = 100

    # TODO!: Read only document len() < nlp.max_length

    texts = [txt for _, txt in zip(range(limit), ds)]
    docs = list(nlp.pipe(texts))

    for doc in docs:
        processed_txt = ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
        counts_line = wc.process_text(processed_txt)
        counts_all.update(counts_line)

    wc.generate_from_frequencies(counts_all)

    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
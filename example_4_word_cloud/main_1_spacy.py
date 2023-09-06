"""Speakleash: basic wordcloud (using spacy)"""

import os
from collections import Counter

from speakleash import Speakleash
import matplotlib.pyplot as plt
import spacy
from wordcloud import WordCloud


if __name__ == '__main__':

    # Select dataset ("wolne_lektury_corpus" is smaller one)
    PROJECT = "wolne_lektury_corpus"

    # Initiating directory
    base_dir = os.path.join(os.path.dirname(__file__))
    replicate_to = os.path.join(base_dir, "datasets")
    print(f"Replicate datasets to: {replicate_to}")

    # Initiating Speakleash
    sl = Speakleash(replicate_to)

    # Get only text from dataset
    ds = sl.get(PROJECT).data

    # Prepare spacy pipe & set maximum text length (considering RAM allocation)
    nlp = spacy.load('pl_core_news_md', disable=["ner", "parser", "tagger", "textcat"])
    nlp.max_length = 200000

    # Prepare texts & process with spacy
    limit = 100
    texts = [txt[:nlp.max_length] for _, txt in zip(range(limit), ds)]
    docs = list(nlp.pipe(texts))

    # Process text and update frequency distribution
    wc = WordCloud(max_font_size=100, max_words=100, background_color="white", contour_width=1)
    counts_all = Counter()

    for _, doc in enumerate(docs):
        processed_txt = ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
        counts_line = wc.process_text(processed_txt)
        counts_all.update(counts_line)

    # Create wordcloud
    wc.generate_from_frequencies(counts_all)
    
    # Display wordcloud
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
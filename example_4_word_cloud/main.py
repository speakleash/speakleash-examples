import os
from collections import Counter

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from speakleash import Speakleash
import spacy

base_dir = os.path.join(os.path.dirname(__file__))
replicate_to = os.path.join(base_dir, "datasets")

sl = Speakleash(replicate_to)
wc = WordCloud()
nlp = spacy.load('pl_core_news_md')
counts_all = Counter()

counter = 0
limit = 100

ds = sl.get("saos").data
for txt in ds:
    doc = nlp(txt)
    processed_txt = ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
    counts_line = wc.process_text(processed_txt)
    counts_all.update(counts_line)
    counter += 1
    if counter > limit:
        break

wc.generate_from_frequencies(counts_all)
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

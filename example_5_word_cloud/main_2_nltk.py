"""Speakleash: basic wordcloud (using nltk)"""

import os

import matplotlib.pyplot as plt
import nltk
from speakleash import Speakleash
from wordcloud import WordCloud


# Stopwords list (from Wikipedia: https://pl.wikipedia.org/wiki/Wikipedia:Stopwords)
stopwords_dict = ["a", "aby", "ach", "acz", "aczkolwiek", "aj", "albo", "ale", "ależ", "ani", "aż", "bardziej", "bardzo", "bo", "bowiem", "by", "byli", "bynajmniej", "być", "był", "była", "było", "były", "będzie", "będą", "cali", "cała", "cały", "ci", "cię", "ciebie", "co", "cokolwiek", "coś", "czasami", "czasem", "czemu", "czy", "czyli", "daleko", "dla", "dlaczego", "dlatego", "do", "dobrze", "dokąd", "dość", "dużo", "dwa", "dwaj", "dwie", "dwoje", "dziś", "dzisiaj", "gdy", "gdyby", "gdyż", "gdzie", "gdziekolwiek", "gdzieś", "i", "ich", "ile", "im", "inna", "inne", "inny", "innych", "iż", "ja", "ją", "jak", "jaka", "jakaś", "jakby", "jaki", "jakichś", "jakie", "jakiś", "jakiż", "jakkolwiek", "jako", "jakoś", "je", "jeden", "jedna", "jedno", "jednak", "jednakże", "jego", "jej", "jemu", "jest", "jestem", "jeszcze", "jeśli", "jeżeli", "już", "ją", "każdy", "kiedy", "kilka", "kimś", "kto", "ktokolwiek", "ktoś", "która", "które", "którego", "której", "który", "których", "którym", "którzy", "ku", "lat", "lecz", "lub", "ma", "mają", "mało", "mam", "mi", "mimo", "między", "mną", "mnie", "mogą", "moi", "moim", "moja", "moje", "może", "możliwe", "można", "mój", "mu", "musi", "my", "na", "nad", "nam", "nami", "nas", "nasi", "nasz", "nasza", "nasze", "naszego", "naszych", "natomiast", "natychmiast", "nawet", "nią", "nic", "nich", "nie", "niech", "niego", "niej", "niemu", "nigdy", "nim", "nimi", "niż", "no", "o", "obok", "od", "około", "on", "ona", "one", "oni", "ono", "oraz", "oto", "owszem", "pan", "pana", "pani", "po", "pod", "podczas", "pomimo", "ponad", "ponieważ", "powinien", "powinna", "powinni", "powinno", "poza", "prawie", "przecież", "przed", "przede", "przedtem", "przez", "przy", "roku", "również", "sama", "są", "się", "skąd", "sobie", "sobą", "sposób", "swoje", "ta", "tak", "taka", "taki", "takie", "także", "tam", "te", "tego", "tej", "temu", "ten", "teraz", "też", "to", "tobą", "tobie", "toteż", "trzeba", "tu", "tutaj", "twoi", "twoim", "twoja", "twoje", "twym", "twój", "ty", "tych", "tylko", "tym", "u", "w", "wam", "wami", "was", "wasz", "wasza", "wasze", "we", "według", "wiele", "wielu", "więc", "więcej", "wszyscy", "wszystkich", "wszystkie", "wszystkim", "wszystko", "wtedy", "wy", "właśnie", "z", "za", "zapewne", "zawsze", "ze", "zł", "znowu", "znów", "został", "żaden", "żadna", "żadne", "żadnych", "że", "żeby"]

# Function to Tokenize the text
def tokenize_text(text: str) -> list[str]:
    '''
    Function to tokenize texts.

    Parameters
    ----------
    text : str
        Text to tokenize...

    Attributes
    ----------
    list[str]
        List of tokenized articles
    '''
    global stopwords_dict
    words = nltk.word_tokenize(text.lower())
    return [word for word in words if (word.isalpha() and word not in stopwords_dict)]


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
    data = sl.get(PROJECT).data

    limit = 100
    texts = [txt for _, txt in zip(range(limit), data)]

    # Tokenize words
    tokunis = list(map(tokenize_text,texts))

    # Create string with all words
    all_words = [word for tokens in tokunis for word in tokens]

    # Frequency Distribution
    word_freq = nltk.FreqDist(all_words)

    # Create wordcloud
    wc = WordCloud(stopwords=set(stopwords_dict), 
                    max_font_size=100, 
                    max_words=100, 
                    background_color="white",
                    contour_width=1).generate_from_frequencies(word_freq)

    # Display wordcloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
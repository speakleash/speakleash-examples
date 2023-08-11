import os
import pandas as pd
import plotly.express as px

from speakleash import Speakleash

SAVE_PATH = "imgs/"


class Chart:
    """Generate .html charts from the dataset."""
    def __init__(self, PROJECT):
        """
        Initialize Chart class.

        Parameters
        ----------
        PROJECT : str
            Name of the dataset to generate charts for.
        """
        self.PROJECT = PROJECT
        base_dir = os.path.join('datasets')
        replicate_to = os.path.join(base_dir, self.PROJECT)
        sl = Speakleash(replicate_to)  
        self.ds = sl.get(self.PROJECT).ext_data
        self.meta_frame = self.get_meta
        self.df_charts = self.get_data

    @property
    def get_meta(self):
        """Extract metadata from the dataset and create DataFrame."""
        lst1 = []
        for doc in self.ds:
            txt, meta = doc
            meta['text'] = txt
            lst1.append(meta)
        meta_frame = pd.DataFrame(lst1)
        return meta_frame

    @property
    def get_data(self):
        """Process metadata and create DataFrame for .html charts."""
        df = self.meta_frame.copy()
        df = df.drop_duplicates(subset=['text'], ignore_index=True)
        cols = ['punctuations', 'symbols', 'stopwords', 'oovs', 'pos_num', 'pos_x', 'capitalized_words']
        for col in cols:
            df[f'{col}_ratio'] = df[col] / df['words']
        df_charts = df[[
            'avg_sentence_length',
            'avg_word_length',
            'verb_ratio',
            'noun_ratio',
            'punctuations_ratio',
            'symbols_ratio',
            'stopwords_ratio',
            'oovs_ratio',
            'lexical_density',
            'camel_case',
            'capitalized_words_ratio',
            'pos_x_ratio',
            'pos_num_ratio',
            'gunning_fog']]
        df_charts = df_charts.assign(quality=df["quality"])
        return df_charts

    def draw_charts(self):
        """Generate and save .html charts."""
        df_charts = self.df_charts
        for i in df_charts.columns:
            if i == "quality":
                pass
            else:
                # Handle non-existing directory for save .html files
                if not os.path.exists(SAVE_PATH):
                    os.makedirs(SAVE_PATH)
                fig = px.histogram(df_charts, x=df_charts[i], y=df_charts[i], nbins=40, color="quality",
                                   category_orders={"quality": ["LOW", "MEDIUM", "HIGH"]},
                                   color_discrete_sequence=px.colors.qualitative.Dark2,
                                   title=(f"{i} by text quality"), text_auto=True, histfunc="count")
                fig.write_html(f"imgs/{self.PROJECT}_{i}_hist.html")


if __name__ == '__main__':
    PROJECT = input('Enter a dataset name: ')
    charts = Chart(PROJECT)
    charts.draw_charts()

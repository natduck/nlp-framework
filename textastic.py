"""
Core framework class for NLP Comparative Analysis
"""
from nltk.corpus import stopwords
from collections import defaultdict
from parser import text_parse, text_clean
from sankey import make_sankey
from exception import import_file_contents
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from afinn import Afinn


class Textastic:
    def __init__(self):
        # manage data about the different texts that
        # we register with the framework
        self.text_data = defaultdict(dict)
        self.stop_words = set()
        self.file_contents = {}

    def load_text(self, filename, label=None):
        """
        Register a document with the framework
        :param filename: (str) Name of the file
        :param label: (str) Label of the file contents
        """
        # Check if user did not input a label
        # if so, make label the file name
        if label is None:
            label = filename

        # import_file_contents()
        with open(filename, "r", encoding='utf8', errors="ignore") as f:
            contents = f.read()
            self.file_contents[label] = text_parse(contents)

            self.text_data["word_count"][label] = len(self.file_contents[label].split())

            afinn = Afinn()
            self.text_data["sentiment_score"][label] = afinn.score(self.file_contents[label])


    def load_stop_words(self, stopfile=""):
        """
        Loads the stop words
        :param stopfile: Name of the file with the list of stop words
        :return:
        """
        self.stop_words = set(stopwords.words("english"))

        if stopfile != "":
            with open(stopfile, "r") as stop_f:
                stop_f_words = stop_f.read()
                stop_f_words = text_parse(stop_f_words)
                stop_f_words = set(stop_f_words.split())
                self.stop_words.update(stop_f_words)

    def wordcount_sankey(self, word_list=None, k=5):
        """
        Creates a Sankey diagram for either word_list that the user chooses OR top k words for each file combined
        :param word_list: List of words included the Sankey diagram
        :param k: Number of top words per file
        """

        word_count_df = pd.DataFrame()
        for label, text in self.file_contents.items():
            text = text_clean(text).split()
            word_count_series = pd.Series(text).value_counts()
            count_df = word_count_series.to_frame()
            count_df = count_df.reset_index()
            count_df.columns = ['word', 'count']
            count_df = count_df.assign(label=label)
            word_count_df = pd.concat([word_count_df, count_df])

        word_count_df = word_count_df[["label", "word", "count"]]
        word_count_df = word_count_df[~word_count_df["word"].isin(self.stop_words)]
        word_count_df['word'] = word_count_df["word"].astype(str)

        # call make sankey
        word_sankey = make_sankey(df=word_count_df,
                                  src="label",
                                  targ="word",
                                  vals="count",
                                  word_list=word_list,
                                  k=k)
        word_sankey.show()

    def wordcloud(self):
        """
        Takes a dictionary and subplots with word clouds for each key-value pair.
        """
        fig, axs = plt.subplots(1, len(self.file_contents), figsize=(20, 10))
        for i, (key, value) in enumerate(self.file_contents.items()):
            # Join all the values of the current key into a single string
            text = ''.join(value)

            # Create the wordcloud for the current key-value pair
            wc = WordCloud(stopwords=self.stop_words, background_color='white').generate(text)

            # Add the wordcloud to the subplot
            axs[i].imshow(wc, interpolation='bilinear')
            axs[i].set_title(key)
            axs[i].axis('off')
        plt.show()

    def sentiment_bar(self):
        """
        Creates and shows a bar chart showing the sentiment score for each text
        """
        df_scores = pd.DataFrame(self.text_data["sentiment_score"].items(), columns=["label", "sentiment_score"])
        df_scores.sort_values("sentiment_score", ascending=False, inplace=True)
        sentiment_bar = px.bar(data_frame=df_scores, x="label", y="sentiment_score", title="Sentiment Score by Text")
        sentiment_bar.show()

"""
Nathan Brito, Kelly Chen, Anh Nguyen, Tung Giang
DS3500 / A Reusable Extensible Framework for Natural Language Processing
Homework 3
Date Created: 2/15/2023 / Date Last Updated: 2/26/2023
"""
#import statements
from textastic import Textastic
import pprint as pp


def main():
  # initialize framework
  tt = Textastic()

  # register text files/parse/clean
  tt.load_text(filename="text_files/boston_25_mbta.txt",
               label="Boston 25 MBTA")
  tt.load_text(filename="text_files/boston_com_mbta.txt",
               label="Boston.com MBTA")
  tt.load_text(filename="text_files/boston_globe_mbta.txt",
               label="Boston Globe MBTA")
  tt.load_text(filename="text_files/WBUR_mbta.txt", label="WBUR MBTA")
  tt.load_text(filename="text_files/wcvb_mbta.txt", label="WCVB MBTA")

  # load stop words
  tt.load_stop_words(stopfile="text_files/stopwords.txt")

  # produce some visualizations

  tt.wordcount_sankey()
  tt.wordcount_sankey(word_list=[
    "mbta", "boston", "blue", "red", "green", "orange", "line", "silver",
    "train"
  ])
  tt.wordcloud()
  tt.sentiment_bar()

  # pp.pprint(tt.data)


if __name__ == '__main__':
  main()

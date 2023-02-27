from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stopwords_list = set(stopwords.words("english"))
punctuations = """!()-![]{};:,+'",<>./?@#$%^&*_~Â""" # List of punctuation to remove

def text_parse(textfile):
    """

    :param textfile: (str) Name of the text file
    :return: parsedReview (str): A
    """
    # split the review into words
    splitReview = textfile.split()
    # take the stubborn punctuations out
    parsedReview = " ".join([word.translate(str.maketrans('', '', punctuations)) + " " for word in splitReview])

    return parsedReview

def text_clean(textfile):
    """
    Excludes stop words and lower cases each character from the text in textfile
    :param textfile: (str) Name of the text file
    :return: clean_review (str) A cleaned version of the text
    """
    clean_words = []
    splitReview = textfile.split()
    for w in splitReview:
        if w.isalpha() and w not in stopwords_list:
            clean_words.append(w.lower())
    clean_review = " ".join(clean_words)

    return clean_review

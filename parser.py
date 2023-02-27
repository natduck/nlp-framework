from nltk.corpus import stopwords

stopwords_list = set(
  stopwords.words("english"))  # A list of stopwords to filter
punctuations = """!()-![]{};:,+'"\,<>./?@#$%^&*_~Â"""  # A list of punctuation to remove


def textParse(textfile):
  """
    Get rid of the punctuations using the punctuations list above
    :param filename (string): Name of the file
    :return: parsedReview (the cleaned words list)
  """
  # split the review into words
  splitReview = textfile.split()
  # take the stubborn punctuations out
  parsedReview = " ".join([
    word.translate(str.maketrans('', '', punctuations)) + " "
    for word in splitReview
  ])

  return parsedReview


def textClean(textfile):
  """
  Select all words that are not in the stopwords list and put them in lower case
  :param filename (string): Name of the file
  :return: clean_review (the lower case words that are also not in the stopword list)
  """
  # initiate an empty list of clean words
  clean_words = []

  # split the text
  splitReview = textfile.split()

  # filter out words that are not in the stopword list and put the others in lower case
  for w in splitReview:
    if w.isalpha() and w not in stopwords_list:
      clean_words.append(w.lower())
  clean_review = " ".join(clean_words)

  return clean_review

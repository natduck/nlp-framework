@staticmethod
    def _default_parser(filename):
        results = {
            'wordcount': Counter("to be or not to be".split()),
            'numwords': rnd.randrange(10, 50)
        }
        return results

if parser is None:  # do default parsing of standard .txt file
        results = Textastic._default_parser(filename)
      else:
        results = parser(filename)
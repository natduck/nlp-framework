"""
Nathan Brito, Kelly Chen, Anh Nguyen, Tung Giang
DS3500 / A Reusable Extensible Framework for Natural Language Processing
Homework 3
Date Created: 2/15/2023 / Date Last Updated: 2/26/2023
"""

class Exception(Exception):
  """
    A class that inherits the Exception class
    
    Attributes:
        message: explanation of the errors
  """
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)
    

def ParserException(Exception, filename):
  """
    Anticipate possible errors to the file
    :param filename: (string) Name of the file
    :return: Errors (if any)
  """
  try:
    with open(filename, 'r') as f:
        contents = f.read()
      
    if not filename:
        raise Exception ("Error: File '{filename}' cannot be found or read.")
    
    if any(not c.isalnum() and c not in [' ', '\n'] for c in contents):
        raise Exception ('Error: Text contains special characters')
    
  except AttributeError:
      raise AttributeError("AttributeError occurred")

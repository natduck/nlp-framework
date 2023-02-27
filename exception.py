"""
Nathan Brito, Kelly Chen, Anh Nguyen, Tung Giang
DS3500 / A Reusable Extensible Framework for Natural Language Processing
Homework 3
Date Created: 2/15/2023 / Date Last Updated: 2/26/2023
"""
from parser import textParse

def ParserException(filename):
  """
    Anticipate possible errors to the file
    :param filename: (string) Name of the file
    :return: Errors (if any)
  """
  try Exception:
    with open(file_name, 'r') as f:
        contents = f.read()
      
  except FileNotFoundError:
      raise FileReadError('File cannot be found')

  if not contents:
      raise EmptyFileError('File is empty')

  if any(not c.isalnum() and c not in [' ', '\n'] for c in contents):
      raise SpecialCharacterError('Text contains special characters')

  # AttributeError 
  except AttributeError:
    raise AttributeError("AttributeError occurred.")
"""
Nathan Brito, Kelly Chen, Anh Nguyen, Tung Giang
DS3500 / A Reusable Extensible Framework for Natural Language Processing
Homework 3
Date Created: 2/15/2023 / Date Last Updated: 2/19/2023
"""


def import_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()

    except FileNotFoundError:
        raise FileReadError('File cannot be found')

    if not contents:
        raise EmptyFileError('File is empty')

    if any(not c.isalnum() and c not in [' ', '\n'] for c in contents):
        raise SpecialCharacterError('Text contains special characters')

    else:
        return

from nltk.tokenize import TweetTokenizer
from spellchecker import SpellChecker

def check(words):
    """
    """
    spell = SpellChecker()
    tknzr = TweetTokenizer()

    # find those words that may be misspelled
    misspelled = spell.unknown(tknzer.tokenize(words))

    for word in misspelled:
        # Get the one `most likely` answer
        print(spell.correction(word))

        # Get a list of `likely` options
        print(spell.candidates(word))

if __name__ == "__main__":
    check()
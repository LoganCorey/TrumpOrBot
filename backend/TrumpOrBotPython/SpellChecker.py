
from nltk.tokenize import TweetTokenizer
from spellchecker import SpellChecker

def check(words):
    """
    """
    spell = SpellChecker()
    tknzr = TweetTokenizer()
    correctedWords = []
    correctedSentence =" "
    allWords = tknzr.tokenize(words)
    # find those words that may be misspelled
    misspelled = spell.unknown(allWords)

    for word in allWords:
        correctWord = ""
        if word in misspelled:
            correctWord = spell.correction(word)
        elif len(word) == 1:
            pass
        else:
            correctWord = word
        correctedWords.append(correctWord)
    return correctedSentence.join(correctedWords)

   # for word in misspelled:
        # Get the one `most likely` answer
      #  print(spell.correction(word))

        # Get a list of `likely` options
     #   print(spell.candidates(word))

if __name__ == "__main__":
    check()
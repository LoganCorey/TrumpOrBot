
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

class DataShaper:
    def __init__(self,  file="SmallerSet.txt"):
        self.file = file
        self.rawText = self._extractTextAndLower()
        self.chars, self.chars_to_int, self.int_to_char = self.createMapping()
        self.n_chars, self.n_vocab = self.createVocab()
        self.dataX, self.dataY, self.n_patterns, self.seq_length= self.sequenceData(self.chars)
        self.X, self.y = self.encodeData()

    def _extractTextAndLower(self):
        text = open(self.file, encoding="utf8").read()
        text = text.lower()
        return text
    
    def _removePuncuation(self, chars):
        removeable = ['\n', '\r', ' ', '!', '"', "'", '(', ')', '*', ',', '-', '.', ':', ';', '?', '[', ']', '_']
      
        for character in chars:
            if character in removeable:
                chars.replace(character,"")
        return chars
    
    def createMapping(self):
        
        chars = sorted(list(set(self.rawText)))
        chars_to_int = dict((c, i) for i, c in enumerate(chars))
        int_to_char = dict((i, c) for i, c in enumerate(chars))

        return chars,chars_to_int, int_to_char
    
    def createVocab(self):
        n_chars = len(self.rawText)
        n_vocab = len(self.chars)
        return(n_chars, n_vocab)

    def sequenceData(self, chars_to_int):
        seq_length = 100
        dataX = []
        dataY = []
        for i in range(0, self.n_chars - seq_length, 1):
            seq_in = self.rawText[i:i + seq_length]
            seq_out = self.rawText[i + seq_length]
            dataX.append([self.chars_to_int[char] for char in seq_in])
            dataY.append(self.chars_to_int[seq_out])
        n_patterns = len(dataX)
        return (dataX, dataY, n_patterns, seq_length)
        
    def encodeData(self):
        # reshape X to be [samples, time steps, features]
        X = numpy.reshape(self.dataX, (self.n_patterns, self.seq_length, 1))
        # normalize
        X = X / float(self.n_vocab)
        # one hot encode the output variable
        y = np_utils.to_categorical(self.dataY)
        return (X,y)

if __name__ == "__main__":
    shaper = DataShaper("test")




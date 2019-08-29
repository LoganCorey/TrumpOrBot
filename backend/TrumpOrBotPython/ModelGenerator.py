import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from DataShaper import DataShaper
import sys
class ModelGenerator:
    def __init__(self, dataShaper):
        self.dataShaper = dataShaper
    
    def generateLSTMModel(self):

        model = Sequential()
        model.add(LSTM(256, input_shape=(self.dataShaper.X.shape[1], self.dataShaper.X.shape[2]), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256))
        model.add(Dropout(0.2))
        model.add(Dense(self.dataShaper.y.shape[1], activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        
        # define the checkpoint
        filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
        checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
        callbacks_list = [checkpoint]
        # define the checkpoint
        filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
        checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
        callbacks_list = [checkpoint]
        model.fit(self.dataShaper.X, self.dataShaper.y, epochs=5, batch_size=200, callbacks=callbacks_list)

    def generateModelWithWeights(self, weights):
        model = Sequential()
        model.add(LSTM(256, input_shape=(self.dataShaper.X.shape[1], self.dataShaper.X.shape[2]), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256))
        model.add(Dropout(0.2))
        model.add(Dense(self.dataShaper.y.shape[1], activation='softmax'))
        model.load_weights(weights)
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        return model

    def predict(self, model):
        # pick a random seed
        start = numpy.random.randint(0, len(self.dataShaper.dataX)-1)
        pattern = self.dataShaper.dataX[start]
      
        print("\"", ''.join([self.dataShaper.int_to_char[value] for value in pattern]), "\"")
        # generate characters
        for i in range(110):
            x = numpy.reshape(pattern, (1, len(pattern), 1))
            x = x / float(self.dataShaper.n_vocab)
            prediction = model.predict(x, verbose=0)
            index = numpy.argmax(prediction)
            result = self.dataShaper.int_to_char[index]
            seq_in = [self.dataShaper.int_to_char[value] for value in pattern]
            sys.stdout.write(result)
            pattern.append(index)
            pattern = pattern[1:len(pattern)]
      


if __name__ == "__main__":
    shaper = DataShaper()
    generator = ModelGenerator(shaper)
   # generator.generateLSTMModel()
    model = generator.generateModelWithWeights("weights-improvement-10-1.7093.hdf5")
    generator.predict(model)
from DataShaper import DataShaper
from SpellChecker import check
from ModelGenerator import ModelGenerator
import sys



if __name__ == "__main__":
    shaper = DataShaper()
    generator = ModelGenerator(shaper)
   # generator.generateLSTMModel()
    model = generator.generateModelWithWeights("weights-improvement-10-1.7665.hdf5")
    original, new = generator.predict(model)
    print(check(new))
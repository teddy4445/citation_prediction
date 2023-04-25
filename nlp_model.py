# library imports
import os
import gensim
from nltk.data import find


class NLPmodel:
    """
    A class to covert text to a fixed-length vector
    """

    def __init__(self):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(str(find('models/word2vec_sample/pruned.word2vec.txt')),
                                                                     binary=False)

    def run(self,
            text: str) -> list:
        return self.model[text]  # should return a 300 dimensional list (vector)

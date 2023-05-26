# library imports
import os
import gensim
import numpy as np
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
        while "  " in text:
            text = text.replace("  ", " ")
        answer = []
        for word in text.split(" "):
            word = word.lower().strip()
            try:
                answer.append(np.array(self.model[word]))
            except:
                pass
        return np.mean(answer, axis=0)

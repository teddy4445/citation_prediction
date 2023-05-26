# library imports
import os
import pickle
import numpy as np
import pandas as pd

# project imports
from consts import *


class MidasTouchClustering:
    """
    A class to check how much Midas-touch
    """

    def __init__(self,
                 model=None):
        self.model = model

    def train(self,
              x_train_static: pd.DataFrame,
              x_train_time_series: pd.DataFrame,
              y_train: pd.DataFrame,
              x_valid_static: pd.DataFrame,
              x_valid_time_series: pd.DataFrame,
              y_valid: pd.DataFrame):
        """
        This function responsible to build a NN for time series with static data
        :param x_train_static: static data for training
        :param x_train_time_series: dynamic data for training
        :param y_train: the y-col for training
        :param x_valid_static: static data for validation
        :param x_valid_time_series: dynamic data for validation
        :param y_valid: the y-col for validation
        :return: None
        """

    def test(self):
        # TODO: finish here later
        pass

    def save_model(self,
                   save_file: str):
        with open(save_file, "wb") as model_file:
            pickle.dump(self.model, model_file)

    @staticmethod
    def load_model(load_file: str):
        with open(load_file, "rb") as model_file:
            model = pickle.load(model_file)
        return MidasTouchClustering(model=model)

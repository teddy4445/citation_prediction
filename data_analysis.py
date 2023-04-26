# library imports
import os
import pandas as pd

# project imports
from consts import *
from citation_prediction_model import CitationPredictionModel


class DataAnalysis:
    """
    A class to analyze the data, generating a time-series model to predict citations over time
    """

    def __init__(self):
        pass

    @staticmethod
    def model_pipeline(df: pd.DataFrame,
                       model_save_path: str = str):
        model = CitationPredictionModel()
        # TODO: split the 'df' to train, validation, and test and than to x_static, x_time_series, and y
        model.train(x_train_static=,
                    x_train_time_series=,
                    y_train=,
                    x_valid_static=,
                    x_valid_time_series=,
                    y_valid=)
        # TODO: finish later
        model.test()
        model.save_model(save_file=model_save_path)
        return model

# library imports
import os
import numpy as np
import pandas as pd

# project imports
from consts import *
from plotter import Plotter
from data_loader import DataLoader
from data_analysis import DataAnalysis


class Main:
    """
    A class to run the main and test the components of model
    """

    def __init__(self):
        pass

    @staticmethod
    def run(prepare_data: bool = False):
        Main.prepare_io()
        data_df = Main.prepare_data(prepare_data=prepare_data)
        Main.analyze_data(df=data_df)

    @staticmethod
    def prepare_io():
        create_paths = [DATA_FOLDER, RESULTS_FOLDER]
        for path in create_paths:
            try:
                os.mkdir(path)
            except Exception as error:
                pass

    @staticmethod
    def prepare_data(prepare_data: bool = False):
        # prepare data
        if prepare_data:
            samples = DataLoader.run(data_path=DATA_FOLDER)
            # save results
            samples.to_csv(PROCESSED_DATA_PATH,
                           index=False)
            # return results
            return samples
        else:
            return pd.read_csv(PROCESSED_DATA_PATH)

    @staticmethod
    def analyze_data(df: pd.DataFrame):
        # generate model and make some relevant models
        model = DataAnalysis.model_pipeline(df=df,
                                            model_save_path=MODEL_PATH)

        # run analysis using the model
        # TODO: add here

        # save the model and the results with some graphs
        # TODO: add here - use the Plotter class, add more methods there if needed


if __name__ == '__main__':
    Main.run(prepare_data=True)

# library imports
import os
import pickle
import numpy as np
import pandas as pd

# NN libraries
from tensorflow import keras


# project imports
from consts import *


class CitationPredictionModel:
    """
    A class that has a ML\DL model to predict time series of citations
    # TODO: you can continue the design I started below or take advantage of https://github.com/sktime/sktime
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
        # TODO: think about the right numbers below here
        n_timesteps = 8
        n_features = 7

        # RNN + SLP Model
        # Define input layer
        recurrent_input = Input(shape=(n_timesteps, n_features), name="TIMESERIES_INPUT")
        static_input = Input(shape=(x_train_static.shape[1],), name="STATIC_INPUT")
        # RNN Layers
        # layer - 1
        rec_layer_one = Bidirectional(
            LSTM(128, kernel_regularizer=l2(0.01), recurrent_regularizer=l2(0.01), return_sequences=True),
            name="BIDIRECTIONAL_LAYER_1")(recurrent_input)
        rec_layer_one = Dropout(0.1, name="DROPOUT_LAYER_1")(rec_layer_one)
        # layer - 2
        rec_layer_two = Bidirectional(LSTM(64, kernel_regularizer=l2(0.01), recurrent_regularizer=l2(0.01)),
                                      name="BIDIRECTIONAL_LAYER_2")(rec_layer_one)
        rec_layer_two = Dropout(0.1, name="DROPOUT_LAYER_2")(rec_layer_two)
        # SLP Layers
        static_layer_one = Dense(64, kernel_regularizer=l2(0.001), activation='relu', name="DENSE_LAYER_1")(
            static_input)
        # Combine layers - RNN + SLP
        combined = Concatenate(axis=1, name="CONCATENATED_TIMESERIES_STATIC")([rec_layer_two, static_layer_one])
        combined_dense_two = Dense(64, activation='relu', name="DENSE_LAYER_2")(combined)
        output = Dense(n_outputs, activation='sigmoid', name="OUTPUT_LAYER")(combined_dense_two)
        # Compile ModeL
        model = Model(inputs=[recurrent_input, static_input], outputs=[output])
        # binary cross entropy loss

        # TODO: if you train this model, it should be regression and not classification
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', f1_m, precision_m, recall_m])

        # TODO: the loss should be MAE or MSE in our case
        model.compile(loss="mae",
                      optimizer='adam',
                      metrics=['accuracy', f1_m, precision_m, recall_m])
        model.summary()

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
        return CitationPredictionModel(model=model)

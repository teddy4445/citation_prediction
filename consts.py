# A file to hold all the consts in the application #
import os

# Names
DATA_FOLDER_NAME = "data"
RESULTS_FOLDER_NAME = "results"

# Paths
DATA_FOLDER = os.path.join(os.path.dirname(__file__), DATA_FOLDER_NAME)
RESULTS_FOLDER = os.path.join(os.path.dirname(__file__), RESULTS_FOLDER_NAME)
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), RESULTS_FOLDER_NAME, "processed_data.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), RESULTS_FOLDER_NAME, "citation_prediction_model")

# MAGIC NUMBERS
ERROR_VAL = -1

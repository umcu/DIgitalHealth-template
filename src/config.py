"""Configuration file."""

import os
from os.path import abspath, dirname, join, realpath


SRC_PATH = dirname(realpath(__file__))
DATA_DIR = abspath(join(SRC_PATH, os.pardir, "data"))

UCI_HEART_DISEASE_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/"
)

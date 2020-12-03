# ===================================
# Calculate mean of columns in .csv
# ===================================

# Functions to build: 
#   specify filepath
#   read csv
#   calculate mean of columns
#   save new csv

# specify imports
from pathlib import Path
import numpy as np
import pandas as pd

# specify filepath
def filepath(pathname, filename): 
    data_dirs = Path(pathname)
    data_path = (data_dirs / filename)
    return data_path

# read csv
def load_table(file): 
    data_input = pd.read_csv(file)
    return data_input

# calculate means
def column_means(data)
    data_output = data.mean(axis=0)
    return data_output

# save new csv
def save_output(data, file):
    data.to_csv(file)
    print('File saved to ', file)
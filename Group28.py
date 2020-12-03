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
with open('testdata.csv')as f:
    f_csv = csv.reader(f)
    column=[]
    for row in f_csv:
        column.append([row[2] for row in f_csv])
# save new csv
def column_means(data):
    data_output = data.mean(axis=1, skipna=True)
    return data_output

# save new csv
def save_output(data, file):
    data.to_csv(file)
    print('File saved to ', file)

# implement full workflow in one function
def load_run_save(dirpath, infilename, outfilename):
    input_path = filepath(dirpath, infilename)
    output_path = filepath(dirpath, outfilename)
    data_input = load_table(input_path)
    data_output = column_means(data_input)
    save_output(data_output, outfilename)

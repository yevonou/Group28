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
import csv

# specify filepath
def filepath(pathname, filename): 
    data_dirs = Path(pathname)
    data_path = (data_dirs / filename)
    return data_path

# read csv
def load_table(file): 
    with open(file, newline='') as csvfile: 
        data_table = csv.reader(csvfile, delimiter-'')
    return data_table

# calculate means

# save new csv
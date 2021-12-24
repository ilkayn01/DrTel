import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import median, mean
import math
from numpy import mean
import os
import glob
from google.colab import files
from math import *
csv_folders = glob.glob("/content/output_folder/dr_tel/*/")

path = os.getcwd()
csv_files = []
for i in csv_folders:
  csv_files.append(glob.glob(os.path.join(f'{i}', "*.csv")))

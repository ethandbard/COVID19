import os
import pandas as pd
import itertools
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import warnings
from datetime import datetime
plt.style.use('fivethirtyeight')

data = pd.read_csv(r'C:\Users\ethan\Documents\R Projects\COVID19 Analysis\cases_clustered.csv')
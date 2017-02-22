import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn import cross_validation

data = pd.read_csv('ex1data1.txt')
print(data)
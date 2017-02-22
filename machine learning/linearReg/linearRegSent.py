import quandl
import pandas as pd

data = quandl.get("WIKI/GOOGL")
print(data.head())
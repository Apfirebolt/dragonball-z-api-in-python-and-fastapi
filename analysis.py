import pandas as pd
import numpy as np

df = pd.read_csv('data/data.csv')

# Get the columns
print(df.columns)
print(df.isnull().sum())
import sys
#from os.path import dirname, abspath
#d=dirname(dirname(abspath(__file__)))
#sys.path.append(d)
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/preprocessing')
import cleaning_data
import pandas as pd
import numpy as np

df = pd.read_csv('../data/houses.csv')
print(df.head())

print(df.columns)
#After preprocessing
print("------------After preprocessing------------------------------")
df = cleaning_data.preprocess(df)

print(df.head())

print(df.columns)

#print("Helloooooooo")
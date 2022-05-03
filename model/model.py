from cgi import test
import sys
#from os.path import dirname, abspath
#d=dirname(dirname(abspath(__file__)))
#sys.path.append(d)
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/preprocessing')
import cleaning_data
import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('../data/houses.csv')
print(df.head())

print(df.columns)
#After preprocessing
print("------------After preprocessing------------------------------")
df = cleaning_data.preprocess(df)

print(df.head())

print(df.columns)

#Defining features and target
y = df['Price']
#Here I will drop our target Price, as well as type of sale since it is only one type and for now I'm dropping location
X = df.drop(columns=['Price', 'Type of sale', 'Location'], axis=1)


#Splitting data into Train and Test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)

#Fitting simple linear regression to training set

model =  LinearRegression()
model.fit(X_train,y_train)

#Save model
filename = "model.sav"
joblib.dump(model, filename)

from cgi import test
import sys
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/model')
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/preprocessing')
import pandas as pd
import numpy as np
import cleaning_data
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def predict(X_test):
    """
    This function will received the data that will be used to predict a new house's price
    """

    
    filename = "../model/model.sav"
    loaded_model = joblib.load(filename)
    
    #Predicting prices 
    #for now predicting on first 
    pred = loaded_model.predict(X_test)

    print("The predicted price is: " + str(pred))

  ###This part is for testing purposes only
df = pd.read_csv('../data/houses.csv')
df = cleaning_data.preprocess(df)
X_test = df.drop(columns=['Price', 'Type of sale', 'Location'], axis=1)
print(X_test.iloc[:1])
predict(X_test.iloc[:1])
#predict(X_test.values[0].reshape(-1,1))
#print(X_test.values.reshape(1,-1)[0])
#predict(X_test.values)
#print(X_test.values.reshape(-1,1))
######



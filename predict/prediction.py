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

    return pred



def train():
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
    r_squared = model.score(X_test, y_test)
    print("R2 score is: "+ str(r_squared))
    #Save model
    filename = "../model/model.sav"
    joblib.dump(model, filename)




###This part is for testing purposes only

#call train() function 

#train()

#df = pd.read_csv('../data/houses.csv')
#df = cleaning_data.preprocess(df)
#X_test = df.drop(columns=['Price', 'Type of sale', 'Location'], axis=1)
#print(X_test.iloc[:1])
#prediction = predict(X_test.iloc[0:1])
#print("The predicted price is: " + str(prediction))
#predict(X_test.values[0].reshape(-1,1))
#print(X_test.values.reshape(1,-1)[0])
#predict(X_test.values)
#print(X_test.values.reshape(-1,1))
######
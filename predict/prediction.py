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

    
    filename = "model/model.sav"
    loaded_model = joblib.load(filename)
    #order of columns after get_dummies --> to avoid problem with data from user
    columns = [
       'Number of bedrooms', 'Living area', 'Furnished', 'Open fireplace',
       'Terrace', 'Garden', 'Surface area land', 'Number of facades', 'Pool',
       'Property subtype_BUNGALOW', 'Property subtype_CHALET',
       'Property subtype_COUNTRY_COTTAGE',
       'Property subtype_EXCEPTIONAL_PROPERTY', 'Property subtype_FARMHOUSE',
       'Property subtype_HOUSE', 'Property subtype_MANOR_HOUSE',
       'Property subtype_MANSION', 'Property subtype_MIXED_USE_BUILDING',
       'Property subtype_OTHER_PROPERTY', 'Property subtype_TOWN_HOUSE',
       'Property subtype_VILLA', 'Kitchen_INSTALLED', 'Kitchen_NOT_INSTALLED',
       'Kitchen_SEMI_EQUIPPED', 'Kitchen_USA_HYPER_EQUIPPED',
       'Kitchen_USA_INSTALLED', 'Kitchen_USA_SEMI_EQUIPPED',
       'Kitchen_USA_UNINSTALLED', 'Condition_GOOD', 'Condition_JUST_RENOVATED',
       'Condition_TO_BE_DONE_UP', 'Condition_TO_RENOVATE',
       'Condition_TO_RESTORE']
    X_test = X_test.reindex(columns = columns, fill_value=0)

    #Predicting prices 
    print(X_test.head())

    
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
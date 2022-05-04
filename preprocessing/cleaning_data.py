import pandas as pd
import numpy as np

def preprocess(df):
    #TODO: Make sure to verify that the columns exists on the df (received by the form) before cleaning with the function checkData
    new_df = df.copy()
    """
    This function will use several functions of this file in order to return a clean df
    """
    #checkData
    new_df = drop_columns(new_df)

    #Convert Booleans to int, empties to 0
    new_df['Furnished'] = new_df['Furnished'].apply(convertToInt)
    new_df['Pool'] = new_df['Pool'].apply(convertToInt)
    new_df['Terrace'] = new_df['Terrace'].apply(convertToInt)
    new_df['Garden'] = new_df['Garden'].apply(convertToInt)
    new_df['Open fireplace'] = new_df['Open fireplace'].apply(convertToInt)

    new_df = imputeAndClean(new_df)
    new_df = creatingDummies(new_df)
    
    return new_df


def checkData(data) -> bool:
    #This is a work in progress
    """
    This function verifies the data received from the form, mandatory data must be given otherwise false is return
    """
    print(str(data))
    df = pd.read_json(data, typ='dictionary')

    if df['Number of facades'] == '' or df['Number of bedrooms'] == '' or  df['Living area'] == '' or  df['Surface area land'] == '':
       return False 
    else:
       return True


def convertToInt(X : int):
    """
    This function receives a value X and converts it to an integer
    Unknown,NaN,False --> 0
    True --> 1
    """
    false_options = ['Unknown',False]
    
    if not X:
         return 0
    elif X in false_options:
        return 0
    else: 
        return 1

def drop_columns(df):
    #This functions returns a dataframe only with the columns I decided to use for my model
    """
    This function receives a df and returns a new df without certain columns and with only residential_sale as Type of Sale 
    """
    new_df = df.copy()
    new_df = new_df.drop(columns = ['Unnamed: 0', 'Garden orientation', 'Terrace orientation', 'Property type' ], axis = 1)
    
    #Keeping only residential sales:
    #Group_sale type of sale only have empty and unknowns on the columns
    new_df = new_df[new_df["Type of sale"]== "residential_sale"]
    
    return new_df


def imputeAndClean(df):
    """
    This function receives a df and returns a new df after eliminating unknown and blanks from some columns and imputing on living area
    """
    new_df = df.copy()
    #dropping properties with blank price, condition or kitchen 
    new_df = new_df.dropna(subset=['Price','Condition','Kitchen'])
    #dropping properties with unknown condition
    new_df = new_df.drop(index=new_df[new_df['Condition']=='Unknown'].index)
    #dropping properties with unknown value for kitchen
    new_df = new_df.drop(index=new_df[new_df['Kitchen']=='Unknown'].index)
    #Impute missing values in living area, replacing by mean
    mean_living_area = new_df['Living area'].mean()

    new_df['Living area'] = new_df['Living area'].fillna(int(mean_living_area))
    
    #Replace unknown in # of facades for NaN and convert to numeric
    new_df['Number of facades']  = new_df['Number of facades'].replace("Unknown", np.NaN)
    new_df['Number of facades']  = pd.to_numeric(new_df['Number of facades'])
    
    #Impute missing values in number of facades replaced by mean
    mean_facades = new_df['Number of facades'].mean()
    new_df['Number of facades'] = new_df['Number of facades'].fillna(int(mean_facades))

    return new_df


def creatingDummies(df):
    """
    This function will create dummies for some categorical variables in the dataset and return the modified dataset
    """
    new_df = df.copy()
    new_df = pd.get_dummies(new_df, columns = ["Property subtype","Kitchen", "Condition"], drop_first = True)
    return new_df



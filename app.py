import numpy as np
import pandas as pd
import sys
import os
import json
import joblib
import importlib.util  
sys.path.append('/model')
sys.path.append('/preprocessing')
sys.path.append('/predict')
#import preprocessing.cleaning_data as cleaning_data
#import predict.prediction as prediction
from preprocessing.cleaning_data import checkData
from preprocessing.cleaning_data import creatingDummies
from predict.prediction import predict_price
#import preprocessing.cleaning_data as cleaning_data
#import predict.prediction as prediction 

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def alive():
    #return '<h1>This is server is alive!</h1>'
    return render_template("serveralive.html")


@app.route('/predict', methods=['POST','GET'])
def predict():
    """
    This function will be use for the prediction of property
    """
    
    if request.method == 'POST':
            number_rooms = request.form.get('number_rooms')
            living_area =  request.form.get('living_area')
            surface_area =  request.form.get('surface_area')
            number_facades =  request.form.get('number_facades')
            furnished = request.form.get('furnisheddropdown')
            terrace = request.form.get('terracedropdown')
            garden = request.form.get('gardendropdown')
            fireplace = request.form.get('fireplacedropdown')
            pool = request.form.get('pooldropdown')
            #REMEMBER: this is property subtype in de df
            property_type= request.form.get('propertydropdown')
            kitchen = request.form.get('kitchendropdown')
            condition = request.form.get('conditiondropdown')
        

            data = {
             'Number of bedrooms':str(number_rooms), 'Living area':str(living_area), 'Furnished':str(furnished), 'Open fireplace' :str(fireplace),
       'Terrace':str(terrace), 'Garden': str(garden), 'Surface area land':str(surface_area), 'Number of facades': str(number_facades),
        'Pool':str(pool), 'Property subtype': str(property_type), 'Kitchen': str(kitchen), 'Condition': str(condition)
            }
            
            json_data=json.dumps(data)
            ##########################
            # passing the file name and path as argument
            spec = importlib.util.spec_from_file_location(
                    "cleaning_data", "preprocessing/cleaning_data.py") 
            print("specc" + str(spec))
            # importing the module as clean
            clean = importlib.util.module_from_spec(spec)       
            spec.loader.exec_module(clean)
            # calling checkdata
            validData = clean.checkData((json_data))

            ##################################
            #validData = cleaning_data.checkData((json_data))
           
            
            if (validData == False):
                return render_template("result.html", result="Please fill in all fields")
            
            else:
                df = pd.DataFrame(data, index=list(range(len(data))))
                df = clean.creatingDummies(df)
                ##########################
                # passing the file name and path as argument
                spec1 = importlib.util.spec_from_file_location(
                    "prediction", "predict/prediction.py") 

                # importing the module as clean
                predicter = importlib.util.module_from_spec(spec1)       
                spec1.loader.exec_module(predicter)
                # calling predicted price
                predicted_price = predicter.predict_price(df)[0]
            ##################################    
               
               # predicted_price = prediction.predict(df)[0]
                
                result_price = str("{:,.2f}".format(predicted_price)) + " EUR"
                return render_template("result.html", result = result_price )

    if request.method == 'GET':
        return render_template("immoeliza.html")
    

if __name__ == '__main__':
    port= int(os.environ.get('PORT',5000))
    app.run(debug=False, host='0.0.0.0', port=port)
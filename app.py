import numpy as np
import sys
import json
import joblib
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/model')
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/preprocessing')
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/predict')
import cleaning_data
import prediction
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def alive():
    return '<h1>This is server is alive!</h1>'


@app.route('/predict', methods=['POST','GET'])
def predict():
    #WIP
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
            #REMEMBER: this is property subtype in de df!!!! 
            property_type= request.form.get('propertydropdown')
            kitchen = request.form.get('kitchendropdown')
            condition = request.form.get('conditiondropdown')
        

            data = {
             'Number of bedrooms':str(number_rooms), 'Living area':str(living_area), 'Furnished':str(furnished), 'Open fireplace' :str(fireplace),
       'Terrace':str(terrace), 'Garden': str(garden), 'Surface area land':str(surface_area), 'Number of facades': str(number_facades),
        'Pool':str(pool), 'Property subtype': str(property_type), 'Kitchen': str(kitchen), 'Condition': str(condition)
            }
            
            json_data=json.dumps(data)
            validData = cleaning_data.checkData((json_data))
            
            if (validData == False):

                print(cleaning_data.checkData(json_data))
                
                return render_template("result.html", result="Please fill in all fields")
            
            else:
                #For now:
                 return render_template("result.html", result="Your prediction will be shown here:")



            #return jsonify(data)
            #result = round(float(ValuePredictor(to_predict_list)), 2)
        #return render_template("home.html", result=result)
        #return render_template("immoeliza.html")
    if request.method == 'GET':
        return render_template("immoeliza.html")
    

if __name__ == '__main__':
   app.run(debug=True)
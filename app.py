import numpy as np
import sys
import joblib
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/model')
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/preprocessing')
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/predict')
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
             'Number of bedrooms':number_rooms, 'Living area':living_area, 'Furnished':furnished, 'Open fireplace' :fireplace,
       'Terrace':terrace, 'Garden': garden, 'Surface area land':surface_area, 'Number of facades': number_facades,
        'Pool':pool, 'Property subtype': property_type, 'Kitchen': kitchen, 'Condition': condition
            }

            return jsonify(data)
            #result = round(float(ValuePredictor(to_predict_list)), 2)
        #return render_template("home.html", result=result)
        #return render_template("immoeliza.html")
    if request.method == 'GET':
        return render_template("immoeliza.html")
    

if __name__ == '__main__':
   app.run(debug=True)
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
            #to_predict_list = request.form.to_dict()
            #to_predict_list = list(to_predict_list.values())
            #to_predict_list = list(map(float, to_predict_list))
            #result = round(float(ValuePredictor(to_predict_list)), 2)
        #return render_template("home.html", result=result)
        return render_template("immoeliza.html")
    if request.method == 'GET':
        return render_template("immoeliza.html")
    

if __name__ == '__main__':
   app.run(debug=True)
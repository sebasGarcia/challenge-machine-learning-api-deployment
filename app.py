import numpy as np
import sys
import joblib
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/model')
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/preprocessing')
sys.path.insert(0, '/Users/sebas/Desktop/BeCode/Projects/challenge-machine-learning-api-deployment/predict')
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
# challenge-machine-learning-api-deployment
Becode ML project, Flask API deployment on Heroku
# Predicting width constrictions during hot rolling

## Description

Arcellor Mittal, in collaboration with BeCode Ghent, assigned us a project where the mission was to build a machine learning model in order to predict the risk of the width constriction during hot-rolling. Valuable and intense brainstorming sessions were involved during the project as well as Exploratory Data Analysis. We propose a decision tree classification model that makes predictions based on the whether a coil has a risk of constriction or not.

![hot-rolling-process](https://ars.els-cdn.com/content/image/1-s2.0-S0924013604013056-gr1.jpg)



![rolling (GIF)](https://upload.wikimedia.org/wikipedia/commons/4/4f/Hydraulic_Piston_driving_BU_Roll_correction.gif)

### Workflow 

The workflow of this project can be illustrated with the image below. Our focus was mainly from step 2, since the data was provided by the client:

![ML Workflow](https://hazaq.me/assets/images/ml-workflow.jpeg)

1. Get Data: We obtained the following data from the client:
* Coil: unique identification: no input
* Furnace number: used reheating furnace. Preferably not used as input, but interesting if the model can be improved with it.
*Analyse: identifier of material type. Categorical, first 3 digits = main group, last digit =  subgroup.
* Hardness: two quantifications of hardness: dimensionless numbers and width: average width in mm.
* Temperature before and after finishing mill: in °C
* Thickness: thickness after finishing mill, in mm
* Thickness profile: information on the shape of the cross section of the strip after finishing. preferably not used as input, but interesting if the model can be improved with it
c, mn, si,…. : chemical composition in parts per million

2. Clean, Prepare & Manipulate Data: During this step we focussed on finding the coils with constrictions, following different methods. Later we decided what data was necessary for model creating and which columns/rows could be dropped. We also performed exploratory data analasys in order to understand the data we needed to manipulate.

3. Train Model: Afterwards we selected two classification models: Decision Tree and Random Forest and trained them with the preprocessed data.

4. Test Data: We tested how the two models performed with the data provided and obtained different metrics such as confusion matrix, accuracy score, recall and precision.

5. Improve: Afterwards we decided to use cross-validation and hyperparameter tuning based on the results of GridSearchCV which determined the best parameters for our model that helped to obtain better results in our metrics. 


### Models

The results obtained from the two selected models are:



#### Confusion Matrix - Decision Tree

![Decision Tree Matrix](https://github.com/bakiguher/arcelor_mittal/blob/sebastian/data/decision%20tree%20matrix.JPG)
#### Confusion Matrix - Random Forest

![Random Forest Matrix](https://github.com/bakiguher/arcelor_mittal/blob/sebastian/data/rf%20matrix.JPG)

Based on those results, we advised the client to utilize Decision Tree Model to assess the risk of constrictions.

###  Repo Architecture 
```

arcelor_mittal
│   README.md                               :This file
│   Exploration Arcelor Mittal Data.ipynb   :Exploration of cleared coildata.csv (includes constriction value)
│   Classification_Model.ipynb              :Model File
│   dsModel.py                              :Desicion Tree Model 
|
│__   
│   data          
│   │ 01_check_measurement_files.py :Reads each coil number from CoilData.csv and checks if it has B4 and B5 measurements.
│   │ 02_collect_stats_140.py       :Script to check stats like mean, std, max, corr 
│   │ 03_collect_stats_120.py       :Script to check stats like ttest, fcor
│   │ 04_combine_stats.py           :Combines all stats in to single file
│   │ showgraph.py                  :Shows a graph of a coil 
│   │ utils.py                      :Helper functions  
```

## Installation

The following software, platforms and tools were utilised during the execution of the project:

* Python 3
* Anaconda Distribution
* Jupyter notebook
* Microsoft Excel
* Pandas library
* Scikit-learn library
* Matplotlib
* Seaborn


## Usage

There are two options to use the application. Both using Heroku:

* App deployed with Docker:
https://immoappheroku.herokuapp.com/predict

* App deployed with Github:




### Contributors:

Sebastián García martínez\
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) https://www.linkedin.com/in/sebastiangarciamartinez](https://www.linkedin.com/in/sebastiangarciamartinez/)
&nbsp;



### Timeline:

7 days

28/04/2022 - 06/05/2022


![Let's do it(GIF)](https://media.giphy.com/media/TgOrB2JA5hqA3Ll4Na/giphy.gif)

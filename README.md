# ML project - Flask API deployment on Heroku with Docker

## Description

The real estate company "ImmoEliza" requires a tool that enables the company to predict property prices using linear regression in order to determine whenever a new property comes on the market, how it should be priced.

After we previously performed a data collection using web scrapping, the company  now asks to create a machine learning model to predict prices on Belgium's real estate sales. The goal is to utilizze this dataset, preprocess to be used with machine learning.

In addition, they require an API to let their web-developers create a website around it, this API ask the useer to Ideally, your API would ask a user to provide with information about a property (features) and return the estimated price using the model.


![sold (GIF)](https://media.giphy.com/media/Q5FVvyM2OuvUUysSQm/giphy.gif)

### Workflow 

The workflow of this project can be illustrated with the image below. The focus was mainly from step 2. Since the data collection took place during a previous project:

![ML Workflow](https://hazaq.me/assets/images/ml-workflow.jpeg)

1. Get Data: The data collection was performed in a previous step, some of the features collected were:
   
- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale (Exclusion of life sales)
- Number of rooms
- Area
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No)
- Garden (Yes/No)
- Surface of the land
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)


2. Clean, Prepare & Manipulate Data: during an Exploratory Data Analysis took place in order to understand the data better as well as possible outlier. The data was cleaning replacing certain blanks as well as dropping certain rows and columns that would not be utilize for the creation of the model.

3. Train Model: for this task a linear regression model was selected and trained.

4. Test Data: the model was tested after performing a split of train/test dataset.

5. Improve: the model is open for improvements in a further version, for intance hyperparameters tuning can be utilized to achieve better predictions. 


### Deployment

After the model was created and tested, the deployment of the Flask app took place, for that Docker and Heroku were utilized:


![deployment](https://miro.medium.com/max/1400/1*qUUVGdw03a0tMKos7W1teg.jpeg)

### Visuals

The Flask application is a simple but functional solution where the user can  first provide the information of the property on the predict page.


### Predict page

![Predict](https://github.com/sebasGarcia/challenge-machine-learning-api-deployment/blob/main/data/predict.JPG)



###  Results page

And then it will provide an estimation price based on the created linear regression model.

![Results](https://github.com/sebasGarcia/challenge-machine-learning-api-deployment/blob/main/data/results.JPG)


###  Repo Architecture 

```
challenge-machine-learning-api-deployment
│   app.py
│   docker-compose.yml
│   Dockerfile
│   Procfile
│   README.md
│   requirements.txt
│
├───data
│       houses.csv
│
├───model
│       model.sav
│
├───predict
│   │   prediction.py
│   │   __init__.py
│   │
│   └───__pycache__
│           prediction.cpython-38.pyc
│           __init__.cpython-38.pyc
│
├───preprocessing
│   │   cleaning_data.py
│   │   EDA and preprocessing.ipynb
│   │   __init__.py
│   │
│   ├───.ipynb_checkpoints
│   │       EDA and preprocessing-checkpoint.ipynb
│   │
│   └───__pycache__
│           cleaning_data.cpython-38.pyc
│           cleaning_data.cpython-39.pyc
│           __init__.cpython-38.pyc
│
└───templates
        immoeliza.html
        result.html
        serveralive.html
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
* Docker 
* Heroku
* Flask


## Usage

There are two options to use the application. Both using Heroku by using any of the following links:

* App deployed with Docker:
https://immoappheroku.herokuapp.com/predict

* App deployed with Github:
https://immoherokuapp.herokuapp.com/predict



### Contributors:

Sebastián García martínez\
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) https://www.linkedin.com/in/sebastiangarciamartinez](https://www.linkedin.com/in/sebastiangarciamartinez/)
&nbsp;



### Timeline:

7 days

28/04/2022 - 06/05/2022


![house(GIF)](https://media.giphy.com/media/TgOrB2JA5hqA3Ll4Na/giphy.gif)

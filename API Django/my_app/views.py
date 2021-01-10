from django.shortcuts import render
import pandas as pd
import requests
import json
import pickle as p
import sklearn
import csv
import numpy as np
from .forms import PredForm
from sklearn.preprocessing import StandardScaler


def get_data():  # used to get an amount of data to see many predictions (75%)
    #dataprocessing in notebook
    data = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")
    data = data.replace("no", False)
    data = data.replace("yes", True)
    data = data.replace("Sometimes", 1)
    data = data.replace("Frequently", 2)
    data = data.replace("Always", 3)
    data["CALC"] = data["CALC"].replace(False, 0)
    data["CAEC"] = data["CALC"].replace(False, 0)
    new_data = data.copy()
    new_data["Male"] = [1 if x == "Male" else 0 for x in new_data["Gender"]]
    new_data["Female"] = [
        1 if x == "Female" else 0 for x in new_data["Gender"]]
    new_data["Walking"] = [
        1 if x == "Walking" else 0 for x in new_data["MTRANS"]]
    new_data["Motorbike"] = [
        1 if x == "Motorbike" else 0 for x in new_data["MTRANS"]]
    new_data["Public_Transportation"] = [
        1 if x == "Public_Transportation" else 0 for x in data["MTRANS"]]
    new_data["Automobile"] = [
        1 if x == "Automobile" else 0 for x in new_data["MTRANS"]]
    new_data["Bike"] = [1 if x == "Bike" else 0 for x in new_data["MTRANS"]]
    new_data = new_data.drop(columns=["Gender", "MTRANS"])

    # importing sklearn to use train_test_split
    from sklearn.model_selection import train_test_split
    df = new_data.drop(columns=['Height', 'Weight', 'NObeyesdad'])
    X = df[df.columns[:-1]]
    Y = df[df.columns[-1]]
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y)  # by default test = 0.25

    dataFrame = x_test
    jsonData = x_test.to_json(orient="split")

    # returning json and dataframe
    return jsonData, dataFrame  # we send only 75% of our data but we could take 100%


def predict_test_set(request):
    jsonData, df = get_data()  # get data threw json and df
    jsonData = json.loads(jsonData)
    jsonData = jsonData["data"]

    # creating model
    modelfile = './clf_model.pickle'
    model = p.load(open(modelfile, 'rb'))

    # predictions on jsonData
    predictions = model.predict(jsonData).tolist()  # get list of predictions
    df["Prediction"] = predictions  # store them in df

    # send results with contex
    results = df.to_json(orient='records')
    context = []
    context = json.loads(results)

    return render(request, 'my_app/prediction_test_set.html',
                  {'data': context})


# home menu
def home(request):
    return render(request, 'my_app/home.html')

# send form to get user data


def pred_one(request):
    f = PredForm()
    return render(request, 'my_app/pred_one.html', {"form": f})


def pred_one_result(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PredForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # clean data and send it with context
            data = form.cleaned_data
            data = [list(data.values())]
            modelfile = './clf_model.pickle'
            model = p.load(open(modelfile, 'rb'))
            ss = StandardScaler()
            data_scaled = ss.fit_transform(data)
            prediction = model.predict(data)[0]
            return render(request, 'my_app/pred_one_result.html', {"pred": prediction})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PredForm()

    return render(request, 'my_app/pred_one_result.html', {'form': form})


def viz(request):
    return render(request, 'my_app/viz.html')

import pandas as pd
from django.shortcuts import render
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def home(request):
    return render(request, "home.html")


def predict(request):
    return render(request, "predict.html")


def result(request):
    diabetes = pd.read_csv(r'C:\Users\Owner\Desktop\diabetes.csv')

    X = diabetes.drop('Outcome', axis=1)
    Y = diabetes['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    input1 = float(request.GET['a1'])
    input2 = float(request.GET['a2'])
    input3 = float(request.GET['a3'])
    input4 = float(request.GET['a4'])
    input5 = float(request.GET['a5'])
    input6 = float(request.GET['a6'])
    input7 = float(request.GET['a7'])
    input8 = float(request.GET['a8'])

    pred = model.predict([[input1, input2, input3, input4, input5, input6, input7, input8]])

    result1= " "
    if pred==[1]:
        result1= "Positive"
    else:
        result1= "Negative"
    return render(request, "predict.html", {"result2": result1})

from re import S
import re
from urllib import response
from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np


KNN_model= pickle.load(open("KNN_flight_model.pkl","rb"))

app=Flask(__name__)

@app.route('/') # codepie.com
def home():
    return render_template('home.html')
    # return "I AM ACTIVE"



@app.route('/predict',methods=["GET","POST"])
def predict():
    if request.method=="POST":
        import pdb; pdb.set_trace()
        dep_time = request.form["Dept_Time"]
        print(dep_time)
        arrival_time = request.form["Arrival_Time"]

        Departure_time=pd.to_datetime(dep_time, format="%Y-%d-%m %H:%M:%S")
        Arrival_time=pd.to_datetime(arrival_time, format="%Y-%d-%m %H:%M:%S")
        
        Stops = int(request.form["stops"])

        Source=request.form["Source"]
        Destination=request.form["Destination"]

        SA=0
        if Source=="Delhi":
            SA=1
        elif Source=="Banglore":
            SA=0
        elif Source=="Chennai":
            SA=3
        elif Source=="Mumbai":
            SA=4
        elif Source=="Kolkata":
            SA=2
        
        DA=0
        if Destination=="Delhi":
            DA=2
        elif Destination=="Banglore":
            DA=0
        elif Destination=="Cochin":
            DA=1
        elif Destination=="Hyderabad":
            DA=3
        elif Destination=="Kolkata":
            DA=4


        Time_minute=abs(Departure_time.hour-Arrival_time.hour)*60

        Knn_mod=KNN_model.predict([[SA, DA, Stops, Time_minute]])
        return render_template("home.html", predictions=Knn_mod)



    
if __name__=="__main__":
    app.run(debug=True)



from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Importing ridge regressor and standard scaler pickle
ridge_model = pickle.load(open('Models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('Models/scaler.pkl','rb'))



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Tempreture=float(request.form.get('Tempreture'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(requst.form.get('DMC'))
        ISI = float(requst.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        scaled_data = standard_scaler.transform([[Tempreture,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(scaled_data)

        return render_template('frontend.html',results=result[0])
    else:
        return render_template('frontend.html')


if __name__=="__main__":
    app.run(host="0.0.0.0",port=4080)

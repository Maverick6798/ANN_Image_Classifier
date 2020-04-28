from flask import Flask, render_template,request
from sklearn.externals import joblib
import pandas as pd
import numpy as np
app= Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict",methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            Age=float(request.form['Age'])
            Estimated_Salary=float(request.form['Estimated_Salary'])
            pred_args=[Age,Estimated_Salary]
            pred_args_arr=np.array(pred_args)
            pred_args_arr=pred_args_arr.reshape(1,-1)
            mul_reg=open("logistic__model.pkl","rb")
            ml_model=joblib.load(mul_reg)
            model_prediction=ml_model.predict(pred_args_arr)

        except ValueError:
            return "Please check if the values are entered correctly!"
        return render_template('predict.html',prediction=model_prediction)


if __name__=='__main__':
    app.run(host='0.0.0.0')



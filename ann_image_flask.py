from flask import Flask, render_template,request
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from PIL import Image
from numpy import asarray
app= Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict",methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            f=request.files['file']
            f.save(f.filename)
            image=Image.open(f)
            newsize=(32,32)
            image=image.resize(newsize)
            data=asarray(image)
            data=data/255
            newinput=32*32*3
            data=data.reshape(1,newinput)
            mul_reg=open("ann_image_model.pkl","rb")
            ml_model=joblib.load(mul_reg)
            model_prediction=ml_model.predict_classes(data)
            if model_prediction==0:
                model_prediction="Plane"
            elif model_prediction==1:
                model_prediction="Automobile"
            elif model_prediction==2:
                model_prediction="Bird"
            elif model_prediction==3:
                model_prediction="Cat"
            elif model_prediction==4:
                model_prediction="Deer"
            elif model_prediction==5:
                model_prediction="Dog"
            elif model_prediction==6:
                model_prediction="Frog"
            elif model_prediction==7:
                model_prediction="Horse"
            elif model_prediction==8:
                model_prediction="Ship"
            elif model_prediction==9:
                model_prediction="Truck"
            
        except ValueError:
            return "Please check if the values are entered correctly!"
        return render_template('predict.html',prediction=model_prediction)


if __name__=='__main__':
    app.run(host='0.0.0.0')



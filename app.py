
import pickle 

from flask import Flask,request,app,render_template,jsonify
import numpy as np
import pandas as pd


app=Flask(__name__)


#load the model
model=pickle.load(open('model.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html',prediction_text='')


@app.route('/predict', methods=['post'])
def predict():
    try:
        data = request.json
        input_data = [
            float(data['co']),
            float(data['nox']),
            float(data['nh3']),
            float(data['no']),
            float(data['no2']),
            float(data['so2']),
            float(data['o3']),
            float(data['pm25']),
            float(data['pm10']),
            float(data['benzene']),
            float(data['toluene']),
            float(data['xylene'])
        ]
        final_input = scaler.transform(np.array(input_data).reshape(1, -1))
        print(f"Transformed input: {final_input}")
        output = model.predict(final_input)[0]
        print(output)
        # return jsonify(prediction_text=f'The Aqi is {output}')
        if 0<output<=50:
            return jsonify(prediction_text='AQI IS GOOD')
        elif 51<=output<=100:
            return jsonify(prediction_text='AQI IS Moderate')
        elif 101<=output<=150:
            return jsonify(prediction_text='AQI IS Unhealthy for sensitive Groups')
        elif 201<=output<=200:
            return jsonify(prediction_text='AQI IS Unhealthy')
        elif 151<=output<=300:
            return jsonify(prediction_text='AQI IS  Very Unhealthy')
        elif 301<=output<=1000:
            return jsonify(prediction_text='AQI IS Hazardous')
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify(prediction_text='An error occurred during prediction.')

if __name__=="__main__":
    app.run(debug=True)

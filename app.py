from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Use JSON data
    Open = float(data['Open'])
    High = float(data['High'])
    Low = float(data['Low'])
    Volume = int(data['Volume'])

    prediction = model.predict([[Open, High, Low, Volume]])
    return jsonify({'predictions': prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
    
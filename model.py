# Build Simple model for practice with Docker and AWS

import pandas as pd

from flask import Flask, jsonify, request, render_template
from sklearn.externals import joblib

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.values
    data = pd.DataFrame(data, index=[0])
    prediction = '${:,.2f}'.format(list(reg.predict(data))[0] * 1000)
    return render_template('index.html', label=prediction)


@app.route('/predictapi', methods=['POST'])
def predictapi():
    json_ = request.get_json()
    query_df = pd.DataFrame(json_, index=[0])
    prediction = list(reg.predict(query_df))
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    reg = joblib.load('model.pkl')
    app.run(host='0.0.0.0', port=5000)

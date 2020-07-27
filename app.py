# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Linear Regression Model
filename = 'final_model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        exp = int(request.form['exp'])

        data = np.array([[exp]])
        my_prediction = classifier.predict(data)
        my_prediction = round(my_prediction[0], 2)

        return render_template('result.html', prediction_text='Employee Salary should be $ {}'.format(my_prediction))

    if __name__ == '__main__':
        # app.run(host='127.0.0.1', port=8001, debug=True)
        app.run(debug=True)

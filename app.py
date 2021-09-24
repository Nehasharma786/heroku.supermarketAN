#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('lr model.pkl', 'rb'))

#User-defined functions/ API Routes
@app.route('/', methods=['GET'])
def supermarket():
    return render_template('supermarket.html')

@app.route('/prediction', methods=['POST'])
def predict():
    total = float(request.form['total'])
    rating = float(request.form['rating'])
    unitprice = float(request.form['unit price'])
    tax = float(request.form['tax'])

    prediction = loadedModel.predict([[total, rating, unitprice, tax]])[0]

    prediction = "$" + str(round(prediction, 2))

    return render_template('supermarket.html', sales_output=prediction)

#Main function
if __name__ == '__main__':
    app.run(debug=True)
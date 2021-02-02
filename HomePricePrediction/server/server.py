from flask import Flask, request, jsonify
import utils

app = Flask(__name__)


@app.route("/get_location_names", methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route("/predict_home_price", methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    response = jsonify({
        'estimated_price': utils.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting Python Flask server for Home Prediction...")
    utils.load_artifacts()
    utils.get_estimated_price('1st Phase JP Nagar', 1000, 3, 3)
    app.run()

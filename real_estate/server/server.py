from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/location')
def get_location():
    response = jsonify({
        "locations": util.get_location_names()
    })
    response.headers('Access-Control-Allow-Origin')
    return response


if "__main__" == __name__:
    print("Starting Python Flask server for Home Price Prediction ...")
    app.run()

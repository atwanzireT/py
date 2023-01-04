from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/location')
def get_location():
    response = jsonify({
        "locations" : util.get_location_names()
    })
    return "Hello World ..."


if "__main__" == __name__:
    print("Starting Python Flask server for Home Price Prediction ...")
    app.run()

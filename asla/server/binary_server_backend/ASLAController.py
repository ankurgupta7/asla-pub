from flask import Flask, request
from flask import Response
import numpy as np
import os
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
app.secret_key = "1234"

@app.route('/train', methods=['POST'])
def make_model():
    """
    Given an Expert user's data dump send this data to the ModelService.
    :return:
    """
    a = np.array([[1, 2], [3, 4]])
    return str(np.mean(a))


@app.route('/getmodel', methods=['POST'])
def get_model():
    """
    Retrieves the global model and sends it back over the HTTP response
    :return:
    """
    if request.method == "POST":
        return request.form["time"]


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

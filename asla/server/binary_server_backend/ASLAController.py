from flask import Flask
from flask import request
from model_generator import ModelGenerator
from classifier import SVM
from databasehelper import DatabaseHelper
import time
import os

app = Flask(__name__)
app.secret_key = "1234"


@app.route('/train', methods=['POST'])
def make_model():
    """
    Given an Expert user's data dump send this data to the ModelService.
    The POST body should contain the flag for storing the data.
    eg:
    {"store":True}
    :return:
    """
    classifier = SVM()
    model_gen = ModelGenerator(classifier)
    model_gen.train()
    if request.form['store'] == 'True':
        model_gen.store_model()
    return "makemodel"


@app.route('/getmodel', methods=["POST"])
def get_model():
    """
    Retrieves the global model and sends it back over the HTTP response
    The POST body should contain the user_model_time.
    eg:
    {"time":20161213-010905;}
    :return:
    """
    user_time = time.strptime(request.form['time'], "%Y%m%d-%H%M%S")
    db_helper = DatabaseHelper()
    latest_global_model = db_helper.get_latest_model()
    for model in latest_global_model:
        model_time = time.strptime(model['time'], "%Y%m%d-%H%M%S")
        if model_time >= user_time:
            return str(model)
        else:
            return "NO"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

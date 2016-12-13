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
    :return:
    """
    classifier = SVM()
    model_gen = ModelGenerator(classifier)
    model_gen.train()
    return "makemodel"


@app.route('/getmodel', methods=["POST"])
def get_model():
    """
    Retrieves the global model and sends it back over the HTTP response
    :return:
    """
    user_time = time.strptime(request.form['time'], "%Y%m%d-%H%M%S")
    db_helper = DatabaseHelper()
    latest_global_model = db_helper.get_latest_model()
    for model in latest_global_model:
        model_time = time.strptime(model['time'], "%Y%m%d-%H%M%S")
        if model_time > user_time:
            return "YES"
        else:
            return "NO "
    return "getmodel"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

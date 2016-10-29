from flask import Flask
from flask import Response
import global_model_service

app = Flask(__name__)


@app.route('/makemodel', methods=['POST'])
def make_model():
    """
    Given an Expert user's data dump send this data to the ModelService.
    :return:
    """
    return "makemodel"


@app.route('/getmodel', methods=['GET'])
def get_model():
    """
    Retrieves the global model and sends it back over the HTTP response
    :return:
    """
    return "getmodel"


if __name__ == '__main__':
    app.run()

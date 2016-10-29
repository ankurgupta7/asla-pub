from pymongo import *
from classifier import Classifier


class GlobalModelService:
    """
    Service that performs global model maintenance
    """

    def __init__(self):
        pass

    @staticmethod
    def fetch_model():
        """
        Fetches the global model and converts it to a HTTP payload compliant format
        :return:
        """
        return None

    @staticmethod
    def generate_model(data):

        """
        Trains a Model and persists it to storage
        :param data: the json data to train with
        :return:
        """
        Classifier.train(data)

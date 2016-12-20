from pymongo import MongoClient  # for interfacing with the mongodb
import time


class DatabaseHelper:
    """
    Class that talks to the database.
    """

    def __init__(self):
        """
        constructor that will init the database connections
        :return: nothing
        """
        self.mongo_client = MongoClient("mongodb://asla-expert:asla@ds149207.mlab.com:49207/trainingdata")
        self.db = self.mongo_client['trainingdata']
        self.model_data = self.db['globalmodeldata']
        self.model = self.db['globalmodel']
        self.scaler = self.db['globalscaler']

    def check_and_fetch(self, force=False):
        """
        This method helps the classifier decide if there is new data that necessitates training.
        :param force: force it to fetch all data regardless
        :return: A mongo db cursor with all the data
        :raises: An exception if there is no new data to train with
        """
        all_data = self.model_data.find()
        if force:
            self.model_data.update_many({"is_trained": "N"}, {"$set": {"is_trained": "Y"}})
            return all_data
        else:
            for datum in all_data:
                if datum["is_trained"] == "N":
                    self.model_data.update_many({"is_trained": "N"}, {"$set": {"is_trained": "Y"}})
                    return all_data
            raise Exception("No new data to train with")

    def get_latest_model(self):
        """
        Fetches the latest global model from the database
        :return: a mongo dbcursor with the latest model
        """
        latest_model = self.model.find().skip(self.model.count() - 1)
        return latest_model

    def get_latest_scaler(self):
        """
        Fetches the latest global model from the database
        :return: a mongo dbcursor with the latest model
        """
        latest_scaler = self.scaler.find().skip(self.scaler.count() - 1)
        return latest_scaler

    def put_model(self, new_model, new_scaler):
        """
        Inserts the model and the scaler in the database.
        :param new_model: the new trained model
        :return: nothing
        """
        time_stamp = time.strftime("%Y%m%d-%H%M%S")
        self.model.delete_many({})  # remove all previous models
        self.model.insert_one({"time": time_stamp, "model": new_model})
        self.scaler.delete_many({})  # remove all previous scaler
        self.scaler.insert_one({"time": time_stamp, "scaler": new_scaler})
        print 'Sent to DB'
        return True

from pymongo import MongoClient  # for interfacing with the mongodb


class databasehelper:
    """
    this class will help the classifier decide if there is new data that necessitates training.
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

    def check_and_fetch(self, force=False):
        """
        Checks if the are untrained datums in the db, if there are it fetches
        :param force: force it to fetch all data regardless
        :return: A mongo db cursor with all the data
        :raises: An exception if there is no new data to train with
        """
        all_data = self.model_data.find()
        if force:
            return all_data
        else:
            for datum in all_data:
                if datum["isTrained"] == "N":
                    return all_data
            raise Exception("No new data to train with")

    def get_latest_model(self):
        """
        Fetches the latest global model from the db
        :return: a mongo dbcursor with the latest model
        """
        latest_model = self.model.find().skip(self.model.count() - 1)
        return latest_model


dbh = databasehelper()
dbh.check_and_fetch()

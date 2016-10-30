from pymongo import MongoClient


class UserAdminService:
    """
    Class that handles all tasks related to user administration
    """

    def __init__(self):
        """
        Constructor. bleh
        :return: nothing
        """
        self.mongo_client = MongoClient("mongodb://asla-website:asla@ds139277.mlab.com:39277/asla-users")
        self.database = self.mongo_client['asla-users']
        self.users = self.db['users']


    @staticmethod
    def make_new_user():
        """
        Makes a new user and puts him in the database
        :return:
        """
        return None

    @staticmethod
    def update_user():
        """
        Updates a user's data
        :return:
        """
        return None

    @staticmethod
    def authenticate_user():
        """
        Authenticates a user or login
        :return:
        """
        return None

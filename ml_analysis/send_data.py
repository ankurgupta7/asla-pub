import glob
import os
import sys

from pymongo import MongoClient

root_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(root_path)


def send_data():
    """Script to send all the csv data to the database"""
    mongo_client = MongoClient("mongodb://asla-expert:asla@ds149207.mlab.com:49207/trainingdata")
    db = mongo_client['trainingdata']
    model_data = db['globalmodeldata']
    header_string = open('headers.csv')
    column_labels = header_string.read().split(',')
    train_path = 'data/*'
    for in_folder in glob.glob(train_path):
        for in_file in glob.glob(in_folder + '/*'):
            print in_file
            data = open(in_file)
            lines = data.readlines()[1:]
            for line in lines:
                data_to_send = {}
                values_per_line = line.split(',')
                for i, j in enumerate(column_labels):
                    data_to_send[j] = values_per_line[i]
                data_to_send['is_trained'] = 'N'
                model_data.insert_one(data_to_send)

if __name__ == '__main__':
    send_data()
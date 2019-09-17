import pymongo
from bson import ObjectId


# CONNECT TO DATABASE
connection = pymongo.MongoClient("localhost", 27017)

# CREATE DATABASE
database = connection['azuredatabase']
# CREATE COLLECTION
collection = database['azuredata']
print("Database connected")


def insert_data(data):
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    document = collection.insert_one(data)
    return document.inserted_id


def update_or_create(document_id, data):
    """
    This will create new document in collection
    IF same document ID exist then update the data
    :param document_id:
    :param data:
    :return:
    """
    # TO AVOID DUPLICATES - THIS WILL CREATE NEW DOCUMENT IF SAME ID NOT EXIST
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged


def get_single_data(document_id):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data


def get_multiple_data():
    """
    get document data by document ID
    :return:
    """
    data = collection.find()
    return list(data)


def update_existing(document_id, data):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    document = collection.update_one({'idno': document_id}, {"$set": data})
    return document.acknowledged


def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged


# CLOSE DATABASE
connection.close()

# =============================================================================
# img='3.jpeg'
# print(img.split('.',1)[0])
# str1='T&C Apply Terms & Conditions Apply WWW.KELLYFELDER.COM #dressthewayyouare 20% OFF FROM DRESSES COLLECTION'
# data3 ={"ocrtext":str1}
# update_existing(img.split('.',1)[0],data3)
# =============================================================================
# =============================================================================
# data=['BUY', 'GET', 'LARGE PAN PIZZA', 'FREE', 'AT PIZZA HUT', 'Valid on 21st August 2019', 'HNB', 'Credit cards', 'Pizza Hut', 'YOUR PARTNER IN PROGRESS']
# str1=' '.join(data)
# data2 ={"string":str1}
# insert_data(data2)
# 
# x= get_multiple_data()
# print(x)
# =============================================================================





from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_URI", "mongodb+srv://test:test@test.0ikxgft.mongodb.net/test?retryWrites=true&w=majority&appName=Test"))
db = client.property_management
properties_collection = db.properties

def get_properties_collection():
    return properties_collection

from pymongo.collection import Collection
from bson import ObjectId
from models import Property, UpdateProperty, PropertyInDB
from typing import List

def create_property(collection: Collection, property: Property) -> List[PropertyInDB]:
    property_dict = property.dict()
    collection.insert_one(property_dict)
    return list(collection.find())

def get_properties_by_city(collection: Collection, city: str) -> List[PropertyInDB]:
    properties = list(collection.find({"city": city}))
    return properties

def update_property(collection: Collection, property: UpdateProperty) -> List[PropertyInDB]:
    property_dict = property.dict()
    _id = property_dict.pop("property_id")
    result = collection.update_one({"_id": ObjectId(_id)}, {"$set": property_dict})
    return list(collection.find())

def get_cities_by_state(collection: Collection, state: str) -> List[str]:
    cities = collection.distinct("city", {"state": state})
    return cities

def get_similar_properties(collection: Collection, property_id: str) -> List[PropertyInDB]:
    property = collection.find_one({"_id": ObjectId(property_id)})
    if property:
        city = property["city"]
        return list(collection.find({"city": city}))
    return []

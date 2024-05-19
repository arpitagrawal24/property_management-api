from pydantic import BaseModel
from bson import ObjectId
from typing import List

class Property(BaseModel):
    property_name: str
    address: str
    city: str
    state: str

class UpdateProperty(BaseModel):
    property_id: str
    property_name: str
    address: str
    city: str
    state: str

class PropertyInDB(Property):
    id: str

class City(BaseModel):
    city: str

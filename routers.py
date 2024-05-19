from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models import Property, UpdateProperty, PropertyInDB, City
from database import get_properties_collection
from crud import create_property, get_properties_by_city, update_property, get_cities_by_state, get_similar_properties
from pymongo.collection import Collection

router = APIRouter()

@router.post("/create_new_property", response_model=List[PropertyInDB])
def create_new_property(property: Property, collection: Collection = Depends(get_properties_collection)):
    return create_property(collection, property)

@router.get("/fetch_property_details", response_model=List[PropertyInDB])
def fetch_property_details(city: str, collection: Collection = Depends(get_properties_collection)):
    properties = get_properties_by_city(collection, city)
    if not properties:
        raise HTTPException(status_code=404, detail="No properties found for the given city")
    return properties

@router.put("/update_property_details", response_model=List[PropertyInDB])
def update_property_details(property: UpdateProperty, collection: Collection = Depends(get_properties_collection)):
    properties = update_property(collection, property)
    if not properties:
        raise HTTPException(status_code=404, detail="Property not found")
    return properties

@router.get("/find_cities_by_state", response_model=List[str])
def find_cities_by_state(state: str, collection: Collection = Depends(get_properties_collection)):
    cities = get_cities_by_state(collection, state)
    if not cities:
        raise HTTPException(status_code=404, detail="No cities found for the given state")
    return cities

@router.get("/find_similar_properties", response_model=List[PropertyInDB])
def find_similar_properties(property_id: str, collection: Collection = Depends(get_properties_collection)):
    properties = get_similar_properties(collection, property_id)
    if not properties:
        raise HTTPException(status_code=404, detail="Property not found")
    return properties

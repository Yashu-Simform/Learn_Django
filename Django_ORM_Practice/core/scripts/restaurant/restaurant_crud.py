from core.models import Restaurant
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

def create_restaurant(*, name, website, latitude, longitude, restaurant_type):

    # 1st way
    # restaurant = Restaurant()
    # restaurant.name = name
    # restaurant.website = website
    # restaurant.latitude = latitude
    # restaurant.longitude = longitude
    # restaurant.date_opened = datetime.now()
    # restaurant.restaurant_type = restaurant_type

    # restaurant.save()

    # 2nd way
    Restaurant.objects.get_or_create(name=name, website=website, latitude=latitude, longitude=longitude, date_opened=datetime.now(), restaurant_type=restaurant_type)
    Restaurant.objects.create(name=name, website=website,latitude=latitude, longitude=longitude, date_opened=datetime.now(), restaurant_type=restaurant_type)

def get_restaurants(filters=...):
    return Restaurant.objects.all()

def get_restaurant(*,id):
    try:
        restaurant = Restaurant.objects.get(id=id)
    except ObjectDoesNotExist as e:
        return {'error': 'Object does not exists.'}

def update_restaurant(*,id, **kwargs):

    # 1. Load the object into memory, update it, and save it
    restaurant = get_restaurant(id=id)
    for key, value in kwargs.items():
        setattr(restaurant, key, value)

    # 2. Update the object directly in the database without loading it into memory
    Restaurant.objects.filter(id=id).update(**kwargs)   # Do not load the object into memory, just update it in the database

def delete_restaurant(*,id):
    try:
        restaurant = Restaurant.objects.get(id=id)
        restaurant.delete()
    except ObjectDoesNotExist as e:
        return {'error': 'Object does not exists.'}
    return {'success': 'Restaurant deleted successfully.'}
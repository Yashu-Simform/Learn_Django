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
    Restaurant.objects.create(name=name, website=website,latitude=latitude, longitude=longitude, date_opened=datetime.now(), restaurant_type=restaurant_type)

def get_restaurants(filters=...):
    return Restaurant.objects.all()

def get_restaurant(*,id):
    try:
        restaurant = Restaurant.objects.get(id=id)
    except ObjectDoesNotExist as e:
        return {'error': 'Object does not exists.'}

def update_restaurant(*,id, **kwargs):
    restaurant = get_restaurant(id=id)
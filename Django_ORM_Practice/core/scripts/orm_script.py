from core.scripts.restaurant import restaurant_crud
from core.models import Restaurant
from django.db import connection

def run():
    print('Script is running...')
    restaurant_crud.create_restaurant(name='marvel', website='https://hoyelmarvel', latitude=111.5, longitude=22.6, restaurant_type=Restaurant.RestaurantTypes.INDIAN)
    # restaurants = restaurant_crud.get_restaurants()
    # print(restaurants)
    print('Script ended...')

    print('\nQueries performed:\n',connection.queries)
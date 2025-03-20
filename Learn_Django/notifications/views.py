from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .db_operations import *
from django.middleware.csrf import get_token

# Create your views here.
def get_notifications(req, p_user_class, p_user_id):
    try:
        allNotifications = get_notifications_db(p_user_class, p_user_id)
        print(allNotifications)
        return JsonResponse(allNotifications, safe=False)
    except Exception as e:
        print(f'Got error while receiving notifications. \n{e}')

    return HttpResponse('All notifications are received!')

def add_notification(req):
    if req.method == 'POST':
        try:
            data = dict(req.POST)
            data.pop('csrfmiddlewaretoken')
            processed_data = {k: data[k][0] for k in data}

            add_notification_db(processed_data)
        except Exception as e:
            print(f'Geting an error while adding notification. \n{e}')
    
        return HttpResponse('Notification added!')
    
    return HttpResponse('Please make a post request!')


def my_get_csrf_token(req):
    csrf_token = get_token(req)
    return JsonResponse({'csrf_token': csrf_token})
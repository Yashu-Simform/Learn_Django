from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .db_operations import *
from django.middleware.csrf import get_token

# Get user's notification
def get_notifications(req):
    try:
        p_user_id = get_userid_from_session(req)
        p_user_class = get_user_class(p_user_id)
        allNotifications = get_notifications_db(p_user_class, p_user_id)
        print(allNotifications)
        return JsonResponse(allNotifications, safe=False)
    except Exception as e:
        print(f'Got error while receiving notifications. \n{e}')

    return HttpResponse('All notifications are received!')

# Add notification
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

#Return the csrf token for any post request want to make
def my_get_csrf_token(req):
    csrf_token = get_token(req)
    return JsonResponse({'csrf_token': csrf_token})

# Extract user id from current session
def get_userid_from_session(req):
    if 'userid' in req.session:
        return req.session['userid']
    return None

# Extract user class from provided user id
def get_user_class(p_user_id):
    if p_user_id[0] == 'T':
        return 'teacher'
    elif p_user_id[0] == 'S':
        return 'student'
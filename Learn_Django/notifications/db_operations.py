from .models import Notification

def get_notifications_db(p_user_class, p_user_id, p_seen = False):
    criteria = {
        'user_class' : p_user_class,
        'user_id' : p_user_id,
        'seen' : p_seen
    }
    try:
        allNotifications = list(Notification.objects.filter(**criteria))
        print(allNotifications)
        result = [dict(title=n.title,message=n.message) for n in allNotifications]
        print(result)
        return result
    except Exception as e:
        raise e
    

def add_notification_db(data):
    try:
        # Pending: Can also check whether specific user exist in db or not 
        print('Adding notification to db')
        print(data)
        anotification = Notification(**data)
        anotification.save()
    except Exception as e:
        raise e
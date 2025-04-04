def saveUserFun(p_body):
    from django.contrib.auth.models import User
    from django.contrib.auth.hashers import make_password
    data = {
        'email': p_body['email'],
        'username': p_body['email'],
        'password': make_password(p_body['password']),
        'last_name': 'none',
        'first_name': 'none',
    }
    user = User.objects.create(**data)

    user.save()
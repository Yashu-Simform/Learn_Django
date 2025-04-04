import requests
import asyncio
from getpass import getpass

def callAPI(p_url, method = 'GET', *args, **kwargs):
    method_map = {
        'GET': requests.get,
        'POST': requests.post,
        'PUT': requests.put,
        'DELETE': requests.delete,
        'PATCH': requests.patch
    }

    req_method = method_map[method]

    get_response = req_method(p_url, *args, **kwargs)

    print(get_response.json())

    return get_response


def getAuthenticate():
    
    # p_username = str(input('Enter username: '))
    # p_password = str(input('Enter password: '))
    password = getpass()

    l_body = {
        'username' : 'worker1',
        'password' : password
    }

    auth_response = callAPI('http://127.0.0.1:8000/auth/', 'POST', json=l_body)
    return auth_response

# def view_teachers_list():

def main():
    auth_response = getAuthenticate() 

    if auth_response.status_code == 200:
        token = auth_response.json()['token']
        headers = {
            'Authorization': f'Token {token}'
        }

        callAPI('http://127.0.0.1:8000/teacher/get_or_create/', headers=headers)
    else:
        print(auth_response)

main()

# asyncio.run(main())
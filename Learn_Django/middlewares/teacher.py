class AuthCheck:
    def __init__(self, response):
        self.response = response
        print('Auth check init ...')

    def __call__(self, request, *args, **kwds):
        print('Auth Check!')

        response = self.response(request)
        
        return response
    
class TokenCheck:
    def __init__(self, response):
        self.response = response
        print('Token check init ...')

    def __call__(self, req, *args, **kwds):
        print('Token Check!')

        response = self.response(req)

        return response
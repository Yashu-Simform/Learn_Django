from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.utils.deprecation import MiddlewareMixin

class AuthCheck(MiddlewareMixin):
    # def __init__(self, response):
    #     self.response = response
    #     print('Auth check init ...')

    # def __call__(self, request, *args, **kwds):
    #     print('Auth Check!')

    #     if not ('loggedin' in request.session):
    #         pass

    #     response = self.response(request)
        
    #     return HttpResponseRedirect(reverse('login'))
    
    def process_request(self, req):
        allowed_urls = ['/login/', '/register/']
        print('Hi by old style')
        if not (True in [req.path.endswith(url) for url in allowed_urls]):
            if req.path.startswith('/teacher/'):
                if (not ('loggedin' in req.session)) or (req.session['loggedin'] == 'False'):
                    #Not have loggedin yet - redirect it to login page
                    print('Redirecting to login page ...')
                    return HttpResponseRedirect(reverse('login'))       # sends response with status code 302 - redirection
        else:
            print('Path match nahi horah he!')
    
class TokenCheck:
    def __init__(self, response):
        self.response = response
        print('Token check init ...')

    def __call__(self, req, *args, **kwds):
        print('Token Check!')

        response = self.response(req)

        return response
    
class BeforeView:
    def __init__(self, response):
        self.response = response
        print('BeforeView is initiated')

    def __call__(self, req, *args, **kwds):
        response = self.response(req)
        return response
    
    def process_view(self, req, *args, **kwargs):
        print('Before view I have played a cricket match.')
        # Can also return HttpResponse
        return None
    
class ExceptionDisplayer:
    def __init__(self, response):
        self.response = response
        print('Exception Displayer initiated!')

    def __call__(self, req, *args, **kwds):
        print('Pre check for exception displayer')
        response = self.response(req)
        print('Post check for exception displayer')
        return response

    def process_exception(self, req, exception):
        print('Exception occured')
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)
    

class ManageTemplate:
    def __init__(self, response):
        self.response = response

    def __call__(self, req, *args, **kwds):
        print('Pre check for Manage Template')
        response = self.response(req)
        print('Post check for Manage Template')
        return response

    def process_template_response(self, req, response):
        print('Adding the loggedin flag')
        response.context_data['loggedin'] = False
        return response
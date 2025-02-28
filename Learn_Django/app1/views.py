from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

def about(request):
    return render(request, 'app1/about.html')

def service(request):
    return render(request, 'app1/service.html')

def contact(request):
    return render(request, 'app1/contact.html')

def getTime(request):
    # timenow = time.time()
    return HttpResponse(f'Time: {int(time.time())}')

def helloBoloHello(request):
    return HttpResponse('<h1>Hello!</h1>')
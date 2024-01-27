from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'users/home.html')
def aboutus(request):
    return render(request, 'users/aboutus.html')
def login(request):
    return render(request, 'users/login.html')


# Create your views here.

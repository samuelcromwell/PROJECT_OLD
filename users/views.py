from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'users/home.html')
def aboutus(request):
    return render(request, 'users/aboutus.html')
def login(request):
    return render(request, 'users/login.html')
def contactus(request):
    return render(request, 'users/contactus.html')
def courses(request):
    return render(request, 'users/courses.html')
def signup(request):
    return render(request, 'users/signup.html')


# Create your views here.

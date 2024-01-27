from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'users/index.html')
def aboutus(request):
    return render(request, 'users/aboutus.html')
def vantage(request):
    return render(request, 'users/vantage.html')

# Create your views here.

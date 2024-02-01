from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')
def admin(request):
    return render(request, 'users/admin.html')
def aboutus(request):
    return render(request, 'users/aboutus.html')
def login(request):
    return render(request, 'users/login.html')
def courses(request):
    return render(request, 'users/courses.html')
def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account has been created successfully')
            return redirect('home')        
    else:
         form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})
       
    

   

# Create your views here.

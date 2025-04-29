from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'fabolous/SplashScreen.html')

  

def register_view(request):
    return render(request, 'register.html')


from django.contrib.auth import authenticate, login


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Login successful!')
        else:
            messages.error(request, 'Username or password is incorrect.')
        

    return render(request, 'fabolous/login.html')

def register_view(request):
    return render(request, 'fabolous/register.html')
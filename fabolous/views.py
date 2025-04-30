# Authors: Dhruvi Soni and Kashish Jadhav

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User  
# view for splash screen
def home(request):
    return render(request, 'fabolous/SplashScreen.html')

# view for login page

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(userName=username, password=password)
        except User.DoesNotExist:
            user = None

        if user:
            request.session['user_id'] = user.id
            request.session['role'] = user.roles.lower()

            if user.roles.lower() == 'admin':
                return redirect('admin_dashboard')
            elif user.roles.lower() == 'engineer':
                return render(request, 'fabolous/nav.html')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'fabolous/login.html')

# admin dashboard 
def admin_dashboard(request):
    user = get_logged_in_user(request)
    if not user or user.roles != 'admin':
        return redirect('login')
    return render(request, 'fabolous/a_dash.html')

#view for user registration
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = full_name
            user.save()
            login(request, user)
            return redirect('home')

    return render(request, 'fabolous/Registaration.html')

# view for questionnaire page

def questionnaire_view(request):
    return render(request, 'fabolous/Health-check Questionaire.html')

# view for custom admin page


def custom_admin(request):
    return render(request, 'fabolous/admin.html')

#view for help page
def help_page(request):
    return render(request, 'fabolous/how_to.html')

# view for user dashboard
def user_dashboard(request):
    return render(request, 'fabolous/u_dash.html')

# view for results
def results_view(request):
    return render(request, 'fabolous/results.html')

# view for settings page
def settings_view(request):
    return render(request, 'fabolous/settingpage.html')

# view for navigation page
def nav_view(request):
    return render(request, 'fabolous/nav.html')

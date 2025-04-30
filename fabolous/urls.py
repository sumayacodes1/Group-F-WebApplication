"""
URL configuration for groupfabolous project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fabolous import views as fabolousViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fabolousViews.home, name='home'),
    path('login/', fabolousViews.login_view, name='login'),  # Map '/login/' to login_view
    path('nav/', fabolousViews.nav_view, name='nav'),  # Map '/nav/' to nav_view
    path('register/', fabolousViews.register_view, name='register'),  # Map '/register/' to register_view
    path('how-to/', fabolousViews.help_page, name='help'),  # Comes before voting
    path('vote/', fabolousViews.questionnaire_view, name='vote'),
    path('results/', fabolousViews.results_view, name='results'),
    path('user-dashboard/', fabolousViews.user_dashboard, name='user_dashboard'),
    path('settings/', fabolousViews.settings_view, name='settings'),
    path('admin-dash/', fabolousViews.admin_dashboard, name='admin_dashboard'),
    path('custom-admin/', fabolousViews.custom_admin, name='custom_admin'),
]

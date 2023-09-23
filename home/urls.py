from django.urls import path
from . import views  # Import views from the current app (assuming this is the app's urls.py)

urlpatterns = [
    path('', views.home, name="home"),  # Define a URL pattern for the 'home' view
]

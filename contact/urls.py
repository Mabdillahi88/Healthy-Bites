from django.urls import path
from contact import views

urlpatterns = [
    # Define a URL path for the contact form view
    path('contact/', views.ContactMessage.as_view(), name='contact'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include("allauth.urls")),
    path('booking/', include('booking.urls')), 
    path('', include('contact.urls')),
    path('', include('menu.urls')),
    path('', include("blog.urls")),
]

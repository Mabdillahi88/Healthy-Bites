from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include("allauth.urls")),
    path('booking/', include('booking.urls')),
    path('contact/', include('contact.urls')),  # Assuming contact has its own views
    path('menu/', include('menu.urls')),  # Assuming menu has its own views
    path('blog/', include("blog.urls")),  # Removed namespace
    path('', include('home.urls')),  # Assuming you have a home app; removed namespace
]

from django.urls import path
from . import views

# Define URL patterns for the blog app
urlpatterns = [
    path("", views.PostList.as_view(), name="blog_home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]

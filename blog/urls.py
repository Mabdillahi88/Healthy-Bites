from django.urls import path
from . import views

# Define URL patterns for the blog app
urlpatterns = [
    path("", views.PostList.as_view(), name="blog_home"),  # Home page showing a list of blog posts
    path(
        '<slug:slug>/', views.PostDetail.as_view(), 
        name='post_detail'  # URL pattern for viewing a single blog post
    ),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),  # URL pattern for liking a blog post
]

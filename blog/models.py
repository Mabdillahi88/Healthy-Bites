from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Define choices for the 'status' field
STATUS = ((0, 'Draft'), (1, 'Posted'))

# Model for blog posts
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Title of the post
    slug = models.SlugField(max_length=200, unique=True)  # URL-friendly slug
    post_id = models.AutoField(primary_key=True)  # Primary key for the post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # Author of the post
    created_date = models.DateTimeField(blank=True)  # Date created
    updated_date = models.DateTimeField()  # Date last updated
    content = models.TextField()  # Content of the post
    featured_image = CloudinaryField('image', default='placeholder')  # Featured image
    excerpt = models.TextField(blank=True)  # Short excerpt of the post
    status = models.IntegerField(choices=STATUS, default=0)  # Status of the post
    likes = models.ManyToManyField(User, related_name='liked_posts')  # Users who liked the post

    class Meta:
        ordering = ['-created_date']  # Order posts by creation date in descending order

    def __str__(self):
        return self.title  # Return the title of the post as its string representation

    def like_count(self):
        return self.likes.count()  # Count the number of likes for the post

# Model for comments on blog posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # The post the comment belongs to
    name = models.CharField(max_length=50)  # Name of the commenter
    email = models.EmailField()  # Email of the commenter
    body = models.TextField()  # Comment content
    created_date = models.DateTimeField(auto_now_add=True)  # Date and time of comment creation
    approved = models.BooleanField(default=False)  # Approval status of the comment

    class Meta:
        ordering = ['created_date']  # Order comments by creation date in ascending order

    def __str__(self):
        return f'Comment {self.body} by {self.name}'  # Return a string representation of the comment

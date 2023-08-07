
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('status', 'created_date')
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ['title', 'content']


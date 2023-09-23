from .models import Comment
from django import forms


# Form configuration for creating and updating Comment instances
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

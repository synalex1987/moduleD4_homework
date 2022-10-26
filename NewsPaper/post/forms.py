from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'post_type', 'category', ]
from django import forms
from .models import Blog, Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'author']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['blog', 'title', 'content']

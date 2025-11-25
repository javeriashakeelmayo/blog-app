from django import forms
from .models import Blog, Post, BlogUser, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'author']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['blog', 'title', 'content']

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = BlogUser
        fields = ['username', 'email','name']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data 
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write  a comment...', 'rows': 3}),
        }
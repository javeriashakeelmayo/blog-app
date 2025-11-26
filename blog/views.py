from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Blog, Post
from .forms import BlogForm, PostForm, SignupForm, CommentForm



class HomeView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'



class AddBlogView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/add_blog.html'
    success_url = reverse_lazy('home')


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('home')



class PostDetailView(View):
    template_name = 'blog/post_detail.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.all()
        form = CommentForm()
        return render(request, self.template_name, {'post': post, 'comments': comments, 'form': form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)
        comments = post.comments.all()
        return render(request, self.template_name, {'post': post, 'comments': comments, 'form': form})



class SignupView(View):
    template_name = 'blog/signup.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})



@method_decorator(login_required, name='dispatch')
class LikePostView(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('post_detail', slug=slug)

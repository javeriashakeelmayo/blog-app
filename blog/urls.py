# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('add-post/', views.add_post, name='add_post'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]

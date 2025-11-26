# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add-blog/', views.add_blog, name='add_blog'),
#     path('add-post/', views.add_post, name='add_post'),
#     path('post/<slug:slug>/', views.post_detail, name='post_detail'),
#     path('signup/', views.Signup, name='signup'),
#     path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
#     path('post/<slug:slug>/like/', views.like_post, name='like_post'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]



from django.urls import path
from .views import HomeView, AddBlogView, AddPostView, PostDetailView, SignupView, LikePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-blog/', AddBlogView.as_view(), name='add_blog'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('post/<slug:slug>/like/', LikePostView.as_view(), name='like_post'),
]

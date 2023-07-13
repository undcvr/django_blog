from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('signup/', register, name='signup'),
    # path('profile/', profile, name='profile'),
    # path('profile_view/<int:pk>/', profile_view, name='profile_view'),
    # path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/<int:pk-1>/', ShowProfilePageView.as_view(), name='profile_view'),
]

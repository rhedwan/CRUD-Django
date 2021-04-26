from django.contrib import admin
from django.urls import path, include
from .views import BlogListView, BlogCreateView, BlogDetailView,BlogUpdateView, BlogDeleteView, BlogIndexView


urlpatterns = [
    path('', BlogListView.as_view(), name='index' ),
    path('home/', BlogIndexView.as_view(), name='home' ),
    path('new/', BlogCreateView.as_view(), name='new'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete') 
]
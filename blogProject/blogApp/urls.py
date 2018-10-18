from django.urls import path, include

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.userIndex, name='user_index'),
    path('news/feed/',views.newsFeed, name='newsFeed')
]
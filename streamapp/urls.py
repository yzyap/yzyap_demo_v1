from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('nesne_ogrenme/', views.nesne_ogrenme, name='nesne_ogrenme'),
    ]
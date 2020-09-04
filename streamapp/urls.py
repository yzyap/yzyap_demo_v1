from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('nesne_ogrenme/', views.nesne_ogrenme, name='nesne_ogrenme'),
    path('learnobject', views.learnobject, name='learnobject'),
    path('signup/',views.SignUpView.as_view(), name='signup'),
    path('validate_username/', views.validate_username, name='validate_username'),    
    ]
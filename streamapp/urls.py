from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('video_feed_processed', views.video_feed_processed, name='video_feed_processed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('blockly_code', views.blockly_code, name='blockly_code'),
    ]
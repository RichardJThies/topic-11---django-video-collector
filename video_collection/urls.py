from django.urls import path
from . import views



#urls used by the app

urlpatterns =[#urls to pages in the app
    path('', views.home, name='home'),#homepage
    path('add', views.add, name='add_video'),#adding videos
    path('video_list', views.video_list, name="video_list")#All the successfully added videos





]








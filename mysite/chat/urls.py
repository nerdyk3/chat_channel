from django.contrib import admin
from django.urls import path
from .views import index,room
 
urlpatterns = [
    path('',index,name='index'),
    path('<room_name>/',room,name='room'),

]
   
from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo, name='demo'),
   # path('about/',views.about,name='about'),
   # path('content/',views.content,name='content'),
    #path('add/',views.addition,name='addition'),
]
from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

    path('',views.show_genres,name='show'),

]
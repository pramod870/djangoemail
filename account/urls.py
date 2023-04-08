from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from .views import CreateRegisterView

urlpatterns = [

    path('', views.user_create, name='usercreate'),
    path('test/', views.test, name='test'),
    path('create', CreateRegisterView.as_view(), name='form_create'),
    path('createrol/', views.CreateView.as_view(), name='create'),
]
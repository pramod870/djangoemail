from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('send_mail/',views.send_mail_to_all, name='send_email'),

]
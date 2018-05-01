from django.contrib import admin
from django.urls import path
from supreme.apps.main import views

urlpatterns = [
    path('', views.MyView.as_view()),
]

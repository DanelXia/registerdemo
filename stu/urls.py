from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path(r'',views.show),
    path(r'register/',views.register),
    path(r'show/',views.show_view)
]


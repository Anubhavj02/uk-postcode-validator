from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    # the url and function to check the postcodes
    path(r'^check/', views.check, name='check'),
]
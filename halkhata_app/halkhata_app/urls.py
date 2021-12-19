from django.urls import path

from . import views

app_name = 'halkhata_app'

urlpatterns = [
    path('', views.home, name='home'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #name identifies this particular url mapping, can use this name to reverse the mapper

]

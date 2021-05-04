from django.contrib import admin
from django.urls import path
from . import views

app_name = "measures"

urlpatterns = [
    path('', views.index, name="index"),
    path('analyze/', views.analyze, name="analyze"),   
    path('measures/', views.set_measure_names, name="measures"),   

]

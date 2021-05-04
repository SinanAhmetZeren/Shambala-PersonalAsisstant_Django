from django.contrib import admin
from django.urls import path
from . import views1

app_name = "todo"

urlpatterns = [
    path('', views1.todos, name="todos"),
    path('update/<int:id>', views1.updatetodo, name="updatetodo"),   
    path('delete/<int:id>', views1.deletetodo, name="deletetodo"),   
    path('add/', views1.addtodo, name="addtodo"),   

]
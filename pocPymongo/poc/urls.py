from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # views.AllToDos.as_view(), name="index"),
    path('add/', views.addTime, name="add"),
    #path('show/', views.getAllTimes)
]

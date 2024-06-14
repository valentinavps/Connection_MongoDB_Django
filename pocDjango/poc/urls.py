from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # views.AllToDos.as_view(), name="index"),
    path('run/', views.runExperiment, name="run"),
    #path('show/', views.getAllTimes)
]

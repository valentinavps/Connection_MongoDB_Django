#from django.conf.urls import url
from django.urls import path, include
#from app.views import poc_list
from .views import (
    PocApiView,
    PocDetail,
)

urlpatterns = [
    
    #path('api', poc_list),
    path('', PocApiView.as_view()),
    path('<int:pk>/', PocDetail.as_view())
]

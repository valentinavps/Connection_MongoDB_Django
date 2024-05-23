import os
import subprocess
from subprocess import Popen, PIPE
from django.shortcuts import render
from .models import time_collection
from django.http import HttpResponse
from django.views.generic.list import ListView
#from utils import get_db_handle

# def get_db_handle():
#     client = MongoClient(host="mongodb://localhost", port=27017)
#     db_handle = client.pocDB.user
#     return db_handle

# class AllToDos(ListView):
#     template_name = "index.html"

#     def get_queryset(self):
#         #template_name = "pocs/index.html"
#         times = time_collection.find()
#         #db = get_db_handle()
#         #results = db.find()
#         return times #HttpResponse(times)
    
def index(request):
    times = time_collection.find()
    print("Entrou")
    context = {
        "Time" : times
    }
    return render(request, 'index.html', context) #HttpResponse("<h1>App is runing ...</h1>")

def addTime(request):
    #time = subprocess.call('./testeTime.sh')
    p = Popen('./testeTime.sh', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    timeByte, err = p.communicate()
    time = timeByte.decode("utf-8")
    print(time)
    records = {
        "Time" : time
    }
    time_collection.insert_one(records)
    return render(request, "add.html", records)

def getAllTimes(request):
   times = time_collection.find()
   return HttpResponse(times)
from django.shortcuts import render
from django.http import HttpResponse
from .models import logs_collection
import os
import subprocess

# Create your views here.

def index(request):
    logs = logs_collection.find()
    #print("Entrou")
    context = {
        "Logs" : logs
    }
    return render(request, 'index.html', context) #HttpResponse("<h1>App is runing ...</h1>") 

def runExperiment(request):
    #subprocess.call('./run-infra.sh')
    os.system("chmod +x ./runExperiment.sh")
    process = subprocess.call('./runExperiment.sh')
    #p = Popen('./testeTime.sh', stdin=PIE, stdout=PIPE, stderr=PIPE)
    #timeByte, err = p.communicate()
    #time = timeByte.decode("utf-8")
    #print(time)
    records = {
        "Test" : "Process requested"
    }
    #time_collection.insert_one(records)
    return render(request, "run.html", records)

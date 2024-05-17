import os
import subprocess
from subprocess import Popen, PIPE
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Poc(models.Model):
    name = models.CharField(max_length = 180, default="")
    #timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    #completed = models.BooleanField(default = False, blank = True)
    #time = datetime.datetime.fromtimestamp(os.system('date +%s')) # +"%FT%T"'))
    #time = subprocess.call('./testeTime.sh')
    p = Popen('./testeTime.sh', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    time, err = p.communicate()
    getTime = subprocess.check_output('date +"%FT%T"', shell=True)
    #getTime.strftime('%Y-%m-%dThh:mm')
    #currentTime = models.DateTimeField(("Date"), default=getTime)
    currentTime = models.CharField(max_length=180, default=time)
    #curentLocalTime = timezone.now()
    #user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task

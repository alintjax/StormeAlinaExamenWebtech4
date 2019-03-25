from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import os.path
import time
import datetime

def formatTime(x):
    days, hours, minutes, seconds_rem = divmod(x, 60)
    # use string formatting with C type % specifiers
    # %02d means integer field of 2 left padded with zero if needed
    return "%02d:%02d:%02d:%02d" % (days, hours, minutes, seconds_rem)

def index(request):
    time = datetime("2019-03-29T22:0:0")
    for x in range(time,-1,-1):
        time.sleep(1)
        print(formatTime(x))
        return HttpResponse(formatTime)
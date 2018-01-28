from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import pytz
from .models import User, Injury

<<<<<<< HEAD
=======
from .learning import getBenchTime
from .unbench import unbench

>>>>>>> 2a6d2bab6b0ada4dc09e894609b885e0ce475795
import codecs
import datetime

import json

def index(request):
    return HttpResponse("You are at the index")

def getUser(request, uid):
    result = User.objects.filter(user_id=uid)
    return HttpResponse(serialize('json',result))

def getUsers(request):
    return HttpResponse(serialize('json', User.objects.all()))

def getInjury(request,uid):
    result = Injury.objects.filter(user_id=uid)
    return HttpResponse(serialize('json',result))

def getInjuries(request):
    return HttpResponse(serialize('json',Injury.objects.all()))

@csrf_exempt
def createUser(request):
     new_id = len(User.objects.all()) + 1
     reader = codecs.getreader("utf-8")
     data = request.read().decode('utf-8')
     data = json.loads(data)
     # print('----------------------------------')
     # print()
     # print(type(data))
     # print()
     # for k,v in data.items():
     #     print(k,v)
     #     print(type(k))
     # print('----------------------------------')
     u = User(name=data['name'],age=int(data['age']),weight=int(data['weight']),height=int(data['height']),user_id=new_id,bucket_name='')
     u.save()

     return HttpResponse("hi")

@csrf_exempt
def createInjury(request):
     reader = codecs.getreader("utf-8")
     data = request.read().decode('utf-8')
     data = json.loads(data)
     u = User.objects.filter(user_id=data['user_id']).values()[0]
     print(getBenchTime(u['age'],u['height'],u['weight'],data['symptoms']))
     i = Injury(user_id=data['user_id'],injury_type=data['injury_type'],symptoms=data['symptoms'],bench_date=timezone.now(),unbench_date=timezone.now())
     i.save()
     return HttpResponse("hi")

@csrf_exempt
def unBench(request):
    reader = codecs.getreader("utf-8")
    data = request.read().decode('utf-8')
    data = json.loads(data)
    i=Injury.objects.filter(user_id=data['user_id'])
    i1=i.values()[len(i)-1]
    j=Injury.objects.filter(bench_date=i1['bench_date']).update(unbench_date=timezone.now())
    j1=Injury.objects.filter(bench_date=i1['bench_date']).values()[0]
    u = User.objects.filter(user_id=data['user_id']).values()[0]
    unbench(u,j1)
    return HttpResponse("hi")

from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from .models import User, Injury

from .learning import getBenchTime
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
     i = Injury(user_id=data['user_id'],injury_type=data['injury_type'],symptoms=data['symptoms'],bench_date=datetime.datetime.now(),unbench_date=None)
     return HttpResponse("hi")

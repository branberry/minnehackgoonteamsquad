from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import User, Injury

def index(request):
    return HttpResponse("You are at the index")

def getUser(request, user_id):  
    return HttpResponse("hi")

def getUsers(request):
    return HttpResponse(serialize('json', User.objects.all()))

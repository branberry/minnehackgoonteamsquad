from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getUser/<int:uid>/',views.getUser,name='getUser'),
    path('getUsers/',views.getUsers,name='getUsers'),
    path('getInjury/<int:uid>/',views.getInjury,name='getInjury'),
    path('getInjuries/',views.getInjuries,name='getInjuries'),
    path('createUser/',views.createUser,name='createUser'),
    path('createInjury/',views.createInjury,name='createInjury'),
]

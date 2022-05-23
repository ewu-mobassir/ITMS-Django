from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
from django.http import HttpResponse


def home(request):
    dict={}
    if request.user.is_authenticated:
        dict['time']= request.user.last_login
    return render(request,'home.html',dict)
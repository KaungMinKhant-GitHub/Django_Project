from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponse

def login(request):
    return render(request,'login/login.html')

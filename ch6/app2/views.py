from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_app2(request):
    return HttpResponse("I am on my_app2")
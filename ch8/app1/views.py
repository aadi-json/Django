from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("I am on the home page")

def my_app1(request):
    return HttpResponse("I am a my_app1")
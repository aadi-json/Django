from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("This is home page")

def myfunction(request):
    return HttpResponse("Hello Django")

def myfunction_2(request):
    return HttpResponse("<H1>Welcome home</H1>")

def learn_mechinelearning(request):
    return HttpResponse("I am currently learning mechine learning")
    
def learn_developement(request):
    return HttpResponse("I am curretly learning developement")
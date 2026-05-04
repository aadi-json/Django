from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myapp(request,**kwargs):
    feelings=kwargs.get("feelings")
    print(feelings)
    return HttpResponse(f"I am inside the home page {feelings}")

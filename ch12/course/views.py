from django.shortcuts import render

# Create your views here.

def learn_flask(req):
    return render(req, 'course/flask.html')

def learn_python(req):
    return render(req, 'course/python.html')
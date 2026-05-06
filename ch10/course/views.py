from  datetime import datetime
from django.shortcuts import render
import time
# Create your views here.


#filters Example-1

# def learn_django(request):
#     name="django"
#     duration="30days"
#     seats=30
#     course_details={"name":name,"duration":duration, "seats":seats}
#     return render(request,'course/django.html',course_details)

#filters Example-2

# def learn_django(request):
#     return render(request,'course/django.html', {"Name":"Django","Description":"Django is a awsome web framework "})

#filters Example-3

# def learn_django(request):
#     date=datetime.now()
#     return render(request,'course/django.html', {"date":date,})

#filters Example-4

def learn_django(request):
    date=datetime.now()
    return render(request,'course/django.html', {"f1": 50.1234, "f2":55.4500, "f3":77.0000})
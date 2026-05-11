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

# #filters Example:4- float filter

# def learn_django(request):
#     date=datetime.now()
#     return render(request,'course/django.html', {"f1": 50.1234, "f2":55.4500, "f3":77.0000})

#filters Example:4- If tag

# def learn_django(request):
#     date=datetime.now()
#     return render(request,'course/django.html', {"status":"Online"})

#filters Example:4.1- If tag

# def learn_django(request):
#     date=datetime.now()
#     return render(request,'course/django.html', {"status":"Online", "Name":"Aditya"})

#filters Example:5 - For loop

# def learn_django(request):
#     date=datetime.now()
#     return render(request,'course/django.html', {"Name":["Aditya","Shasta","Harsh","Poonam","Vijeeta"]})

#filters Example:5.1 - For loop with empty tag

# def learn_django(request):
#     date=datetime.now()
#     return render(request,'course/django.html', {"Name":[]})

#filters Example:5.2 - For loop with counter

# def learn_django(request):
#     date=datetime.now()
#     return render(request,'course/django.html', {"Name":["Aditya","Shasta","Harsh","Poonam","Vijeeta"]})

#filters Example:5.2 - how to access complex data

def learn_django(req):
    stu = {
        'stu1': {'name': 'Rahul', 'roll': 101},
        'stu2': {'name': 'Sonam', 'roll': 102},
        'stu3': {'name': 'Raj', 'roll': 103},
        'stu4': {'name': 'Anu', 'roll': 104},
    }

    students = {'student': stu}

    return render(req, 'course/django.html', context=students)
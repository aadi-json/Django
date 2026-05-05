from django.shortcuts import render

# Create your views here.

# def learn_django(request):
#     name="django"
#     duration="30days"
#     seats=30
#     course_details={"name":name,"duration":duration, "seats":seats}
#     return render(request,'course/django.html',course_details)

def learn_django(request):
    return render(request,'course/django.html', {"Name":"Django","Description":"Django is a awsome web framework "})
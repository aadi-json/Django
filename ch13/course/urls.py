from django.urls import path
from course.views import learn_flask, learn_python

urlpatterns = [
    path('py/', learn_python),
    path('fk/',learn_flask)
]
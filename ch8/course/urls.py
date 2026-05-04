from django.urls import path
from course.views import learn_ML
urlpatterns = [
    path('ML/',learn_ML)
]

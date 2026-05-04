from django.urls import path
from course.views import django_course, fastapi_course
urlpatterns = [
    path('dj/', django_course),
    path('fst/', fastapi_course)
]
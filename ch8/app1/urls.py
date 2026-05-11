from django.urls import path
from app1.views import home,my_app1
urlpatterns = [
    path('',home),
    path('app1/',my_app1)
]
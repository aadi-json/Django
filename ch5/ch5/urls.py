"""
URL configuration for ch5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('1/',views.myfunction , name='myfunction'),
    path('2/',views.myfunction_2 , name='myfunction_2'),
    path('3/',views.learn_mechinelearning , name='learn_mechinelearning'),
    path('4/',views.learn_developement , name='learn_developement'),

]

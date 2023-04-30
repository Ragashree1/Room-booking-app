"""roomBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from .views import login1, home, student, student_bookings

urlpatterns = [
    path("admin/", admin.site.urls), 
     path('student/',student, name='student'),
    path("accounts/", include('django.contrib.auth.urls'),),
    path('login/', login1, name='login'),
    path('students/bookings/', student_bookings, name='student_bookings'),

]



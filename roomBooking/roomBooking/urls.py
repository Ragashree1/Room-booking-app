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
from .views import login1, home, student, student_bookings, staff, makeBooking, staffModify ,payment, roomModify, modify_booking 

urlpatterns = [
    path("admin/", admin.site.urls), 
    path('student/',student, name='student'),
    path('staff/', staff, name='staff'),
    path("accounts/", include('django.contrib.auth.urls'),),
    path('login/', login1, name='login'),
    path('students/bookings/', student_bookings, name='student_bookings'),
    path('student/makeBooking/',makeBooking, name='makeBooking'),
    path('staff/staff_modify/',staffModify, name='staff_modify' ),
    path('students/payment/',payment, name='payment' ),
    path('staff/modify/',roomModify, name="modifyRoom" ),
    path('student/modifyB',modify_booking, name='modify_booking')

]



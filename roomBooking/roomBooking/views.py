from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from roomBooking.models import User, Reservation,Room
from django.contrib.auth.decorators import login_required

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
        user = authenticate(request, username=username, password=password)
        if user is None or user.user_type != user_type:
            messages.error(request, 'invalid username or password')
            return render(request, 'registration/login.html')
        else:
            request.user = user
            login(request, user)
            if user.user_type == 'S':
                return student(request)
            elif user.user_type == 'T':
                return render(request,'registration/staff.html')
    else:
        return render(request, 'registration/login.html')
        
def student(request):
    return render(request, 'registration/student.html')
def home(request):
    return render(request, 'registration/home.html')


@login_required
def student_bookings(request):
    bookings = Reservation.objects.select_related('room').filter(user=request.user)
    print(bookings)
    return render(request, 'registration/bookingList.html', {'bookings': bookings})
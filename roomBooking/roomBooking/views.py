from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from roomBooking.models import User, Reservation,Room
from django.contrib.auth.decorators import login_required
from .forms import make_booking
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta

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
            request.session.save()
            login(request, user)
            if user.user_type == 'S':
                return redirect('student')
            elif user.user_type == 'T':
                return redirect('staff')
    else:
        return render(request, 'registration/login.html')
        
def student(request):
    
    today = datetime.today()
    monday = today - timedelta(days=today.weekday())
    currentWeek = [{'day': monday + timedelta(days=i), 'month': (monday + timedelta(days=i)).strftime('%B'), 'dayOfWeek':(monday + timedelta(days=i)).strftime('%A') } for i in range(7)]
    bookings = Reservation.objects.select_related('room').filter(user=request.user)
    context = {
         'week' : currentWeek,
         'bookings': bookings
    }
    return render(request, 'registration/student.html', context)

def staff(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'registration/staff.html', context)

def staffModify(request):
     #pass in more content
     room_name = request.POST.get('r_name')
    #  room_name = request.GET.get('r_name')
     print(room_name)
     room = get_object_or_404(Room, pk=room_name)
     context = {
        'room': room
    }
     return render(request, 'registration/staff_modify.html', context)
def home(request):
    #  login(request, request.user)
     if request.user.user_type == 'S':
                return render(request,'registration/student.html')
     else:
        return render(request,'registration/staff.html')

def makeBooking(request):
    #  if request.method == 'POST':
    #       form = make_booking( request.POST)

    #       if form.is_valid():
    #            print(form.cleaned_data)
    #            return redirect(reverse('student'))

    #  else:
    #       form = make_booking()
     return render(request, 'registration/makeBooking.html', context={'user':request.user})

@login_required
def student_bookings(request):
    bookings = Reservation.objects.select_related('room').filter(user=request.user)
    request.session.save()
    return render(request, 'registration/bookingList.html', {'bookings': bookings, 'user':request.user.name})

def payment(request):
     if request.method == 'POST':
          return render(request, 'registration/payment.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from roomBooking.models import User, Reservation,Room
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from decimal import Decimal

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
         'bookings': bookings,
         'user': request.user.name
    }
    return render(request, 'registration/student.html', context)

def staff(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
        'user': request.user.name
    }
    return render(request, 'registration/staff.html', context)

def staffModify(request):
     room_name = request.POST.get('r_name')
     room = get_object_or_404(Room, pk=room_name)
     context = {
        'room': room,
        'user': request.user.name
    }
     return render(request, 'registration/staff_modify.html', context)
def home(request):
     if request.user.user_type == 'S':
                return render(request,'registration/student.html')
     else:
        return render(request,'registration/staff.html')

def makeBooking(request):
    context = {
        'user':request.user,
        'rooms': Room.objects.all()
    }

    return render(request, 'registration/makeBooking.html', context=context)

@login_required
def student_bookings(request):
    bookings = Reservation.objects.select_related('room').filter(user=request.user)
    request.session.save()
    return render(request, 'registration/bookingList.html', {'bookings': bookings, 'user':request.user.name})

def payment(request):
     if request.method == 'POST':
          room = get_object_or_404(Room, name=request.POST.get('room-name'))
          price = room.price
          start_time = datetime.strptime(request.POST['start-time'], '%H:%M').time()
          end_time = datetime.strptime(request.POST['end-time'], '%H:%M').time()

            # Calculate the duration
          duration = datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), start_time)

            # Access the duration in hours
          duration_hours = duration.total_seconds() / 3600

          amount = price * Decimal(duration_hours)
          if room.promotional_codes is not None and room.promotional_codes != '':
               if request.POST.get('promocode') == room.promotional_codes:
                    amount = amount * Decimal(0.75)
          context = {
               'price': price,
               'room': request.POST.get('room-name'),
               'date': request.POST.get('date'),
               'start_time':request.POST.get('start-time'),
               'end_time':request.POST.get('end-time'),
               'amount': amount,
          }
          return render(request, 'registration/payment.html', context=context)

def success(request):
      if request.method == 'POST':
           room = get_object_or_404(Room, name=request.POST.get('room-name'))
           date = request.POST.get('date')
           start_time = request.POST.get('start-time')
           end_time = request.POST.get('end-time')  
          #  price = Decimal(request.POST.get('price'))
           reservation = Reservation(user=request.user, room=room, time_slot=start_time,end_time= end_time, date=datetime.strptime(date, "%Y-%m-%d"))
           reservation.save()
           return redirect('student_bookings')


def roomModify(request):
     room = get_object_or_404(Room, name=request.POST.get('room-name'))
     if request.POST.get('modType') == 'modify':
          room.location = request.POST.get('room-location')
          room.capacity = request.POST.get('room-capacity')
          room.price = request.POST.get('price-per-hour')
          room.promotional_codes = request.POST.get('room-promotion-code')
          days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
          # availability = {}

          for day in days:
               room.availability[day] = day.lower() in request.POST
               print('helllfdskjl')
               print(day)
               print(day.lower() in request.POST)
          room.save()
          return redirect('staff')
     else:
        room.delete()
        return redirect('staff')
     

def changeBooking(request):
     reservation = get_object_or_404(Reservation, id=request.POST.get('id'))
     if request.POST.get('modType') == 'modify':
          reservation.room = get_object_or_404(Room, name=request.POST.get('room-name'))
          reservation.date = request.POST.get('booking-date')
          reservation.time_slot = request.POST.get('start-time')
          reservation.end_time = request.POST.get('end-time')
          reservation.save()
          return redirect('student_bookings')
     else:
        reservation.delete()
        return redirect('student_bookings')
     

def modify_booking(request):
     reservation = get_object_or_404(Reservation, id=request.POST.get('id'))
     date = reservation.date.strftime('%Y-%m-%d')
     context = {
          'reservation': reservation,
          'user': request.user,
          'date': date,
          'rooms': Room.objects.all(),
          'start_time': reservation.time_slot.strftime('%H:%M'),
          'end_time': reservation.end_time.strftime('%H:%M')
     }
     return  render(request, 'registration/student_modifyBooking.html', context=context)

def confirmCreateRoom(request):
     if request.method == "POST":
          name = request.POST.get('room-name')
          location = request.POST.get('room-location')
          capacity = request.POST.get('room-capacity')
          price = request.POST.get('price-per-hour')
          promo = request.POST.get('room-promotion-code')
          
          days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
          availability = {}

          for day in days:
               availability[day] = day.lower() in request.POST
               print(day)
               print(day.lower() in request.POST)

          # availability['Monday'] = 'monday' in request.POST
          
          room = Room(name=name, location=location, capacity=capacity, price=price, is_available=False, promotional_codes=promo, availability= availability)
          room.save()
          return redirect('staff')
     

def createRoom(request):
      context = {
        'user':request.user
      }
      return render(request, 'registration/createRoom.html', context=context)

def activateRoom(request):
     if request.method == "POST":
          room = get_object_or_404(Room, name=request.POST.get('r_name'))
          if room.is_available:
               room.is_available = False;
          else:
               room.is_available = True;
          room.save()
          return redirect('staff')
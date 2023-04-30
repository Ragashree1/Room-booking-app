#DO NOT RUN THIS FILE , THE BELLOW DATA HAS ALREADY BEEN ADDED
from roomBooking.models import Reservation, Room
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()
user =  User.objects.create_user(username="10200345", name="Kim",password='1234', user_type="S")
user.save()

# Create more rooms
room = Room(name="B.4.10", location="Block B", capacity=10, price=2.00)
room2 = Room(name="A.2.20", location="Block A", capacity=20, price=2.00)
room3 = Room(name="B.3.30", location="Block B", capacity=15, price=2.00)
room4 = Room(name="A.4.14", location="Block A", capacity=12, price=2.00)
room.save()
room2.save()
room3.save()
room4.save()

# Create bookings for the user
reservation = Reservation(user=user, room=room, time_slot='10:00:00', date='2023-05-01')
reservation2 = Reservation(user=user, room=room2, time_slot='14:00:00', date='2023-05-03')
reservation3 = Reservation(user=user, room=room3, time_slot='11:00:00', date='2023-05-05')
reservation4 = Reservation(user=user, room=room4, time_slot='16:00:00', date='2023-05-07')
reservation.save()
reservation2.save()
reservation3.save()
reservation4.save()

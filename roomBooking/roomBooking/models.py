from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    promotional_codes = models.CharField(max_length=50, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    USER_TYPE_CHOICES = {
        ('S', "Student"),
        ('T', "Staff")
    }
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=now)
    end_time = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, default="Booked")

    def __str__(self):
        return f"{self.user} reserved {self.room} from {self.start_time} to {self.end_time}"



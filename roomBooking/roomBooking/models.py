from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db import models
from datetime import datetime, timedelta

class Room(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
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
    name = models.CharField(max_length=50, default='Kim')

    def __str__(self):
        return self.username
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time_slot = models.TimeField(default='09:00:00')
    end_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Booked")
    date = models.DateField(default=now)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['room', 'time_slot', 'date'], name='room_time_slot_pk')
        ]

    def __str__(self):
        return f"{self.user} reserved {self.room} at {self.time_slot} on {self.date}"

    def calculate_end_time(self):
        start_time = datetime.strptime(str(self.time_slot), '%H:%M:%S').time()
        end_time = (datetime.combine(datetime.min, start_time) + timedelta(hours=1)).time()
        return end_time

    def save(self, *args, **kwargs):
        if not self.id:
            if self.end_time is None:
                self.end_time = self.calculate_end_time()
        super().save(*args, **kwargs)







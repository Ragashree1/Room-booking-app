from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = {
        ('S', "Student"),
        ('T', "Staff")
    }
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return self.username

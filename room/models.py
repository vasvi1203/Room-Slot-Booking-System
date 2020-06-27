from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.timezone import now

# Database creation for slot booking
class Booking(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    date = models.DateField(default = timezone.now)
    time_start = models.TimeField(default = timezone.now)
    time_end = models.TimeField(default = timezone.now)
    room_number = models.CharField(max_length = 50)

    # to show on admin page
    def __str__(self):
        return self.customer
    
    def __str__(self):
        return str(self.date)

    def __str__(self):
        return self.time_start

    def __str__(self):
        return self.time_end

    def __str__(self):
        return self.room_number

class Room(models.Model):
    room_number = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.room_number
    
class Slot(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    date = models.DateField(default = timezone.now)
    time_start = models.TimeField(default = timezone.now)
    time_end = models.TimeField(default = timezone.now)
    status = models.CharField(max_length = 50, default = "available")

    def __str__(self):
        return str(self.date)

    def __str__(self):
        return str(self.time_start)

    def __str__(self):
        return str(self.time_end)

    def __str__(self):
        return (self.status)
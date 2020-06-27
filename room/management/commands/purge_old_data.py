# purge_old_data.py

from django.core.management.base import BaseCommand, CommandError
from room.models import Booking, Room, Slot
from datetime import datetime, timedelta, date

class Command(BaseCommand):
    help = 'Delete objects'

    def handle(self, *args, **options):
        def deldate():
            Booking.objects.filter(date__lt = date.today()).delete()
            Slot.objects.filter(date__lt = date.today()).delete()
            self.stdout.write('Deleted objects older than 1 day')
        def deltime():
            Booking.objects.filter(time_end__lte = datetime.now().time()).delete()
            Slot.objects.filter(time_end__lte = datetime.now().time()).delete()
            self.stdout.write('Deleted objects older than current time')

        deldate()
        deltime()
from django.contrib import admin
from .models import Booking, Room, Slot
admin.site.site_header = "Room Manager"
admin.site.site_title = "Room Manager"
admin.site.index_title = "Welcome to the Room Slot Booking Manager Area!"

class RoomManager(admin.ModelAdmin):
	list_display = ["customer", "date", "time_start", "time_end", "room_number"]
	list_filter = ('date',)

class SlotInline(admin.TabularInline):
	model = Slot
	extra = 1

class RoomAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields' : ['room_number']}),]
	inlines = [SlotInline]
	
#admin.site.register(Room)
#admin.site.register(Slot)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, RoomManager)

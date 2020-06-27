from django.urls import path
from . import views

# app_name = 'room'

urlpatterns = [
    path('', views.home, name='room-home'),
    path('about/', views.about, name='room-about'),
    path('book/<int:date_id>/', views.book, name='room-book'),
    path('book/booked/<int:room_id>', views.booked, name = 'room-booked'),
    path('bookings/', views.bookings, name = 'bookings'),
    path('bookings/<int:room_id>/delete', views.delete, name='booking-delete'),
    #path('bookings/<int:room_id>/', views.BookingsDetailView.as_view(), name='booking-detail'),
    #path('bookings/<int:room_id>/delete', views.BookingsDeleteView.as_view(), name='booking-delete'),
    # path('book/booked', views.booked, name='room-booked'),
]

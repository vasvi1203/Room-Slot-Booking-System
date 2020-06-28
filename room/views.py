from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Room, Slot, Booking
from datetime import datetime, timedelta, date
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, DetailView
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# get rooms

rooms = Room.objects.all().order_by('room_number')

def home(request):    
    request.session['on_date'] = datetime.now().strftime("%B %d, %Y")
    return render(request, 'room/home.html', {'date':date.today()})

def about(request):
    return render(request, 'room/about.html', {'title':'About'})

@login_required
def book(request, date_id):
    page = request.GET.get('page', 1)
    paginator = Paginator(rooms, 10)
    try:
        prooms = paginator.page(page)
    except PageNotAnInteger:
        prooms = paginator.page(1)
    except EmptyPage:
        prooms = paginator.page(paginator.num_pages)
    dates = []
    for i in range(14):
        dates.append(date.today() + timedelta(days=i))
    if request.method == 'POST':
        d = request.POST.get('date_id')
        on_date = datetime.strptime(d, "%B %d, %Y").date()
        request.session['on_date'] = d
        context = {
            'rooms' : prooms,
            'dates' : dates,
            'on_date' : on_date,
        }
    else:
        on_date = datetime.strptime(request.session['on_date'], "%B %d, %Y").date()
        context = {
            'rooms' : prooms,
            'dates' : dates,
            'on_date' : on_date,
        }
    
    return render(request, 'room/book.html', context)

@login_required
# show time slot booked
def booked(request, room_id):
    # model = Booking  
    if request.method == 'POST':
        slots = request.POST.get('room_id').split('|')
        number = slots[0].strip()
        request.session['number'] = number
        slot = slots[1]
        slot_list = slot.split('-')
        s = slot_list[0].strip()
        start = datetime.strptime(s, '%I:%M %p')
        e = slot_list[1].strip()
        end = datetime.strptime(e, '%I:%M %p')
        d = slots[2].strip()
        date = datetime.strptime(d, "%B %d, %Y").date()
        creator = request.user
        u = User.objects.get(username__iexact=creator)
        email = u.email
        b = Booking(customer = creator, date = date, time_start = start, time_end = end, room_number = number)
        b.save()
        room_booked = Slot.objects.filter(room = room_id, date = date, time_start = start, time_end = end, status = "available")
        room_booked.update(status = 'booked')
        msg = EmailMessage(
            subject='Booking confirmed!',
            body='Your booking:\nDate : ' + str(d) + '\nRoom No. : ' + number + '\nTime Slot : ' + str(s) + ' to ' + str(e),
            to=[email],
        )
        msg.send()
    context = {
        'number':number,
        'slot':slot,        
        'creator':creator,
    }
    messages.success(request, f'Booking confirmed! Booking details have been mailed to you.')
    return render(request, 'room/home.html', {'date':date.today()})

@login_required
def bookings(request):
    request.session['on_date'] = datetime.now().strftime("%B %d, %Y")
    creator = request.user
    bookings = Booking.objects.filter(customer = creator).order_by('-date')
    context = {
        'bookings':bookings,
        'date':date.today(),
    }
    return render(request, 'room/bookings.html', context)

@login_required
def delete(request, room_id):
    try:
        if request.method == 'POST':
            slots = request.POST.get('room_id').split('|')
            number = slots[0].strip()
            request.session['number'] = number
            slot = slots[1]
            slot_list = slot.split('-')
            s = slot_list[0].strip()
            start = datetime.strptime(s, '%I:%M %p')
            e = slot_list[1].strip()
            end = datetime.strptime(e, '%I:%M %p')
            d = slots[2].strip()
            date = datetime.strptime(d, "%B %d, %Y").date()
            creator = request.user
            u = User.objects.get(username__iexact=creator)
            email = u.email
            i = Room.objects.get(room_number = number)
            b = Booking.objects.get(customer = creator, date = date, time_start = start, time_end = end, room_number = number)
            b.delete()
            room_booked = Slot.objects.filter(room = i.id, date = date, time_start = start, time_end = end, status = "booked")
            room_booked.update(status = 'available')
            send_mail(
                subject='Booking deleted☹!',
                message='Your booking for ' + number + ' on ' + str(d) + ' for the time slot ' + str(s) + ' to ' + str(e) + ' has been deleted.',
                recipient_list=[email],
                fail_silently=False,
            )

    except:
        print('Booking does not exist!') 
    messages.success(request, f'Booking deleted!')
    return redirect(bookings)


'''class BookingsDetailView(DetailView):
    model = Booking
    pk_url_kwarg = 'room_id'            # template name = <app>/<model>_<viewtype>.html

class BookingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    success_url = '/'
    pk_url_kwarg = 'room_id'
    
    def test_func(self):
        booking = self.get_object()
        if self.request.user == booking.customer:
            return True
        else:
            return False'''
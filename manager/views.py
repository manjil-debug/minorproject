from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import venu, customer_requests, customer_register
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def fillupform(request):
    if request.method == "POST":
        data = request.POST
        date = data['date_input']
        name = data['name']
        ph_number = data['ph_number']
        email = data['email']
        venue = data['venue']
        event_type = data['type']
        per_request = data['requests']

        obj = customer_requests.objects.create(date=date,
                                               name=name,
                                               ph_number=ph_number,
                                               email=email,
                                               venue=venue,
                                               event_type=event_type,
                                               per_request=per_request)
        if obj:
            messages.success(request, 'Your Booking was Successful')
        else:
            messages.error(request, 'Your Booking was not-Successful please try again later')

    results = venu.objects.all()
    return render(request, 'fillupform.html', {"venu": results})


def user_login(request):
    return render(request, 'user_login.html')


def sign_up(request):
    if request.method == "POST":
        data = request.POST
        f_name = data['first_name']
        l_name = data['last_name']
        email = data['email']
        ph_number = data['ph_number']
        password = data['password']

        obj = customer_register.objects.create(f_name=f_name,
                                               l_name=l_name,
                                               email=email,
                                               ph_number=ph_number,
                                               password=password)
        if obj:
            messages.success(
                request, 'Your request was Successful, You will receive and email shortly')
        else:
            messages.error(
                request, 'Failed to register please try again later')

    return render(request, 'sign_up.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact_us.html')


def soltee(request):
    return render(request, 'venues/soltee.html')


def sangrila(request):
    return render(request, 'venues/sangrila.html')


def annapurna(request):
    return render(request, 'venues/annapurna.html')


def himalayan(request):
    return render(request, 'venues/himalayan.html')


def dhulikhel(request):
    return render(request, 'venues/dhulikhel.html')



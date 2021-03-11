from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import venu,customer_requests
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'index.html')


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
    return render(request,'fillupform.html', {"venu":results})



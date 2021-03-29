from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import venu, customer_requests, customer_register
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def index(request):
    if request.session.has_key('u_name'):
        u_name = request.session['u_name']
        messages.success(request, 'You are logged-in '+u_name)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def fillupform(request):
    if request.session.has_key('u_name'):
        if request.method == "POST":
            data = request.POST
            date = data['date_input']
            name = data['name']
            ph_number = data['ph_number']
            email = data['email']
            venue = data['venue']
            event_type = data['type']
            per_request = data['requests']

            if customer_requests.objects.filter(date=date, venue=venue).exists():
                messages.error(request, 'The Date is already booked for the venue please select a different date or '
                                        'venue')
            else:
                obj = customer_requests.objects.create(date=date, name=name, ph_number=ph_number, email=email, venue=venue, event_type=event_type, per_request=per_request)
                if obj:
                    messages.success(request, 'Your Booking was Successful')
                else:
                    messages.error(request, 'Your Booking was not-Successful please try again later')

        results = venu.objects.all()
        return render(request, 'fillupform.html', {"venu": results})
    else:
        return redirect('user_login')


def user_login(request):
    if request.session.has_key('u_name'):
        return render(request,'index.html')
    else:
        if request.method == "POST":
            data = request.POST
            u_name = data['u_name']
            password = data['password']
            if customer_register.objects.filter(u_name=u_name, password=password).exists():
                obj = request.session['u_name'] = u_name
                if obj:
                    return redirect('/')
            else:
                messages.error(request, 'login failed')

    return render(request, 'user_login.html')


def logout(request):
    try:
        del request.session['u_name']
        messages.warning(request,'You have logged out')
    except:
        pass
    return redirect('/')


def sign_up(request):
    if request.method == "POST":
        data = request.POST
        f_name = data['first_name']
        l_name = data['last_name']
        u_name = data['u_name']
        email = data['email']
        ph_number = data['ph_number']
        password = data['password']

        obj = customer_register.objects.create(f_name=f_name,
                                               l_name=l_name,
                                               u_name=u_name,
                                               email=email,
                                               ph_number=ph_number,
                                               password=password)
        if obj:
            messages.success(request, 'Your request was Successful, You will receive and email shortly')
        else:
            messages.error(
                request, 'Failed to register please try again later')

    return render(request, 'sign_up.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        msge_name = request.POST['name']
        msge_email = request.POST['email']
        msge_message = request.POST['message']

        obj = send_mail(
                'message from ' + msge_name + ' using email ' + msge_email,
                msge_message,
                msge_email,
                ['eventure.322@gmail.com'],
                )
        if obj:
            return render(request, 'contact_us.html', {'sender': msge_name})
        else:
            messages.error(request, 'Failed to register please try again later')

    return render(request, 'contact_us.html')


def soltee(request):
    results = venu.objects.get(name='Soltee')
    return render(request, 'venues/soltee.html',{"price": results})


def sangrila(request):
    results = venu.objects.get(name='Sangrilaa')
    return render(request, 'venues/sangrila.html',{"price": results})


def annapurna(request):
    results = venu.objects.get(name='Annapurna')
    return render(request, 'venues/annapurna.html',{"price": results})


def himalayan(request):
    results = venu.objects.get(name='himalayan')
    return render(request, 'venues/himalayan.html',{"price": results})


def dhulikhel(request):
    results = venu.objects.get(name='Dhulikhel Resort')
    return render(request, 'venues/dhulikhel.html',{"price": results})



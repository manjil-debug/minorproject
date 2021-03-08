from django.shortcuts import render,redirect
from .models import venu
# Create your views here.


def index(request):
    return render(request,'index.html')

def fillupform(request):
    results = venu.objects.all()
    return render(request,'fillupform.html', {"venu":results})

def gallery(request):
    return render(request,'gallery.html')
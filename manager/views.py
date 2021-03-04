from django.shortcuts import render,redirect
# Create your views here.


def index(request):
    return render(request,'index.html')

def fillupform(request):
    return render(request,'fillupform.html')

    

def gallery(request):
    return render(request,'gallery.html')
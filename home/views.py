from django.shortcuts import render
from .models import meno_veladat,meno_shahadat,madahy1
from django.contrib import messages
from .forms import madahy
def meno(request):
    if request.method == 'POST':
        a = meno_shahadat.objects.all()
        background = 'background-image: linear-gradient(to right, rgb(255, 0, 0), #3d0000)'
        background_button = 'linear-gradient(to left, rgba(0,255,60,0.68), rgba(0,255,209,0.73))'
    else:
        background_button = 'background-image: linear-gradient(to left, rgb(183,0,0), rgb(147,0,0))'
        background = 'linear-gradient(to right, rgb(0, 128, 255), #00a6ff)'
        a = meno_veladat.objects.all()
    return render(request,'meno.html', {'mozoat': a, 'background': background,'background_button':background_button})
def meno2(request , hazrat):

    a = madahy1.objects.filter(daste=hazrat)
    return render(request , 'meno2.html', {'mozoat': a})
def madahy2(request,id):
    a = madahy1.objects.filter(id=id)
    return render(request, 'madahy.html', {'mozoat': a})
def create(request, hazrat):
    a = madahy()
    return render(request , "create.html",{'form': a,'hazrat' : hazrat})

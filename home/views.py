from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Reported
import os
from .forms import *


def index(request):
    return render(request,'index.html')


def find(request):
    return render(request,'find.html')


def report(request):

    return render(request,'Report.html')


def reported(request):

    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('thankyou')
    else:
        form = ReportForm()

    return render(request,'Reported.html',{'form': form})


def success(request):
    search = request.POST.get('search')
    data = Reported.objects.raw(f'select * from home_reported where srn is NULL and (name like "%{search}%" or description like "%{search}%")')
    use = {
        "id": data
    }
    return render(request,'Reported.html',use)


def thankyou(request):
    return render(request,'thankyou.html')
from django.shortcuts import render
from .models import cattle, janu, ramu
from django.http import HttpResponse
import requests


# Create your views here.

def log(request):
    logs = cattle.objects.all()
    context = {'logs': logs}
    return render(request, 'cattlelog/main.html', context)


def fulldetail(request):
    detail = janu.objects.all()
    context = {'detail': detail}
    return render(request, 'cattlelog/janu.html', context)


def ramudetail(request):
    ramu_detail = ramu.objects.all()
    context = {'ramu_detail': ramu_detail}
    return render(request, 'cattlelog/ramu.html', context)

from django.shortcuts import render
from django.conf import settings
from json import load

def home(request):
    return render(request, "personal_finance_home.html")
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import News

def show_main(request):
    context = {
        'app' : 'inifootballshop',
        'name': 'Moch Raydzan',
        'kelas': 'D'
    }

    return render(request, "main.html", context)

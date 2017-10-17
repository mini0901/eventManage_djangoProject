from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello git!!,hello from the other sideeee.....")

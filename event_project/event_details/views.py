from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     return HttpResponse("begining of this APP ,cheers everybody!")

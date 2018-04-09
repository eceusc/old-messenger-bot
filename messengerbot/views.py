from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Front page of ECEUSC Messenger Bot should go here!')

def webhook(request):
    return HttpResponse('Lol lets do this')


from django.http import HttpResponse


def index(request):
    return HttpResponse('Front page of the ECE USC server!')

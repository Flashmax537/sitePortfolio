from django.shortcuts import render
from apps.main.models import Service

def index(request):
    """ main page """
    context = {}
    services = Service.objects.all()
    context['services'] = services

    template = 'index.html'
    return render(request, template, context)
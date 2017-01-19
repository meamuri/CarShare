from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'car_share/index.html')


def trips(request):
    template = loader.get_template('car_share/trips.html')
    context = {
        'data': None,
    }
    return HttpResponse(template.render(context, request))

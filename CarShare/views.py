from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import TravellingForm
from .models import Travelling


def index(request):
    return render(request, 'car_share/index.html')


def trips(request):
    template = loader.get_template('car_share/trips.html')
    context = {
        'data': Travelling.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def add_trip(request):
    if request.method == "POST":
        form = TravellingForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            return redirect('/trips')
    else:
        form = TravellingForm()
        return render(request, 'car_share/add.html', {'form' : form})
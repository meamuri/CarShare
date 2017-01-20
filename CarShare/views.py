from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .forms import TravellingForm, TravellingDeleteForm
from .models import Travelling


def index(request):
    return render(request, 'car_share/index.html')


def trips(request):
    template = loader.get_template('car_share/trips.html')
    context = {
        'travellings': Travelling.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def add_trip(request):
    if request.method == "POST":
        form = TravellingForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            trip.created_at = timezone.now()
            return redirect('/trips')
    else:
        form = TravellingForm()
        return render(request, 'car_share/add.html', {'form' : form})


def to_book(request, id):
    res = get_object_or_404(Travelling, pk=id)
    context = {
        'fullname': res.driver_fullname,
        'phone': res.phone,
        'car': res.car_model,
    }
    form = TravellingDeleteForm(request.POST, instance=res)
    if not form.is_valid():
        return redirect('/')

    res.delete()
    return render(request, 'car_share/info.html', context)
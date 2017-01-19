from django.contrib import admin
from .models import Car, Trip, Passenger, Driver

admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Passenger)
admin.site.register(Trip)

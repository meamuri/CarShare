from django import forms
from .models import Travelling


class TravellingForm(forms.ModelForm):
    class Meta:
        model = Travelling
        fields = ('city_from', 'city_to', 'start_time','end_time', 'phone', 'driver_fullname', 'car_model',)

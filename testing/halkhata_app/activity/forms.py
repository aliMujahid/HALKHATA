from django import forms
from django.db.models import fields

from .models import Ride


class AddRideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['name', 'distance', 'duration',
                  'avg_speed', 'elev_gain', 'cal_burned']
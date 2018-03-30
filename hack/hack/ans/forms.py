from django import forms
from datetime import datetime, date, time

Choices = [
        ('Select', 'Select'),
        ('London', 'London'),
        ('New York', 'New York'),
        ('Los Angeles', 'Los Angeles'),
        ('Chicago', 'Chicago'),
        ('Boston', 'Boston'),
        ('Seattle', 'Seattle'),
        ('Las Vegas', 'Las Vegas'),
        ('Greenwich', 'Greenwich')
]

class Myform(forms.Form):
    lat = forms.DecimalField()
    lon = forms.DecimalField()
    ele = forms.DecimalField()
    # time = forms.DateTimeField()

class NayaForm(forms.Form):
    city = forms.ChoiceField(choices = Choices)

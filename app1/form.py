from django import forms
from django.forms import ModelForm
from .models import *

class patiance_form(ModelForm):

    class Meta:

        model = patient
        fields = '__all__'
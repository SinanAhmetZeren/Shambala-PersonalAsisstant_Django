from django import forms
from .models import measure_values, measure_names

class measure_values_Form(forms.ModelForm):
    class Meta:
        model = measure_values
        fields = ['measure_date', 'measure_1', 'measure_2', 'measure_3', 'measure_4', 'measure_5', 'measure_6']


class measure_names_Form(forms.ModelForm):
    class Meta:
        model = measure_names
        fields = ['measure_1_name', 'measure_2_name', 'measure_3_name', 'measure_4_name', 'measure_5_name', 'measure_6_name']

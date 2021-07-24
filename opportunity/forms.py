from django import forms
from . models import Opportunity

class DateInput(forms.DateInput):
    input_type = 'date'

class OpportunityForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Opportunity
        fields = ("title","budjet","is_negotiatable","description","start_date","end_date","category","industry")

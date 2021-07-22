from django import forms
from . models import Opportunity

class OpportunityForm(forms.ModelForm):
    
    class Meta:
        model = Opportunity
        fields = ("title","budjet","is_negotiatable","description","start_date","end_date","category","industry")

from django import forms
from . models import Opportunity

class DateInput(forms.DateInput):
    input_type = 'date'

class OpportunityForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Opportunity
        fields =  '__all__'
        exclude = ('advertiser',)
    
    def __init__(self, *args, **kwargs):
        self.advertiser = kwargs.pop('advertiser')
        super(OpportunityForm, self).__init__(*args, **kwargs)


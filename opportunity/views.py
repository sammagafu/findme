from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Opportunity
from . forms import OpportunityForm
# Create your views here.


class OpportunityCreateView(CreateView,LoginRequiredMixin):
    model = Opportunity
    form_class = OpportunityForm
    template_name = "opportunity/create.html"

    def form_valid(self, form):
        form.instance.advertiser = self.request.user
        return super().form_valid(form)

class OpportunityListView(ListView,LoginRequiredMixin):
    model = Opportunity
    template_name = "opportunity/list.html"
    context_object_name = "opportunity"
import opportunity
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from django.views.generic import CreateView,ListView,DetailView,UpdateView,RedirectView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


from . models import Opportunity,AppliedJob,SavedJob
from . forms import OpportunityForm
from opportunity import models
from accounts.models import CustomUser

class OpportunityListView(LoginRequiredMixin,ListView):
    model = Opportunity
    template_name = "opportunity/list.html"
    context_object_name = "opportunity"

class OpportunityDetailView(LoginRequiredMixin,DetailView):
    model = Opportunity
    context_object_name = "opportunity"
    template_name = "opportunity/detail.html"


class OpportunityCreateView(LoginRequiredMixin,CreateView):
    form_class = OpportunityForm
    template_name = "opportunity/create.html"
    success_url = reverse_lazy("dashboard:index")

    def form_valid(self, form):
        form.instance.advertiser = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(OpportunityCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['advertiser'] = self.request.user
        return kwargs


class MyOpportunitiesListView(LoginRequiredMixin,ListView):
    model = Opportunity
    template_name = "opportunity/my-opportunities.html"
    context_object_name = "opportunity"

    def get_queryset(self):
        return super().get_queryset().filter(advertiser=self.request.user)
        
class OpportunityUpdateView(LoginRequiredMixin,UpdateView):
    model = Opportunity
    fields = ['title','description','start_date','end_date','category','industry','budjet']
    template_name = "opportunity/edit.html"


class MysavedOpportunity(LoginRequiredMixin,ListView):
    model = SavedJob
    template_name = "opportunity/list-saved.html"
    context_object_name = "opportunity"

    def get_queryset(self):
        return super().get_queryset().filter(saving=self.request.user)

class MyAppliedOpportunity(LoginRequiredMixin,ListView):
    model = AppliedJob
    template_name = "opportunity/list-saved.html"
    context_object_name = "opportunity"

    def get_queryset(self):
        return super().get_queryset().filter(applying=self.request.user)


class SaveOpportunity(LoginRequiredMixin,View):

    model = SavedJob
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        opportunity = get_object_or_404(Opportunity,slug=slug)
        saved = self.model()
        saved.job = opportunity
        saved.saving = self.request.user
        messages.success(self.request, 'Job Applied Succesful, Wait for the results')
        saved.save()

        return redirect('opportunity:list')

class ApplyFOrjob(LoginRequiredMixin,View):
    model = AppliedJob
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        opportunity = get_object_or_404(Opportunity,slug=slug)
        apply = self.model()
        apply.job = opportunity
        apply.applying = self.request.user
        apply.save()
        messages.success(self.request, 'Job Applied Succesful, Wait for the results')
        return redirect('opportunity:list')
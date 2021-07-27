import dashboard
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from accounts.forms import UserProfileForm,CompanyProfileForm
from django.contrib import messages
from django.shortcuts import redirect
from opportunity.models import Opportunity
from accounts.models import CompanyProfile


# Create your views here.


class DashboardView(TemplateView,LoginRequiredMixin):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['posted_jobs'] = Opportunity.objects.filter(is_active=True).count()
        return context

class Profile(TemplateView,LoginRequiredMixin):
    template_name = "dashboard/profile.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['userForm'] = UserProfileForm(instance=self.request.user.profile)
        context['companyForm'] = CompanyProfileForm(instance=self.request.user)
        
        return context



# class CompanyProfileCreateView(CreateView,LoginRequiredMixin):
#     model = CompanyProfile
#     form_class = CompanyProfileForm
#     template_name = 'dashboard/profile.html'	

#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super().form_valid(form)



    
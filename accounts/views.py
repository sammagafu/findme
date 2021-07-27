from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from .models import CustomUser,Profile,CompanyProfile
from .forms import CustomUserCreationForm,UserProfileForm,CompanyProfileForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class FreelanceCreateView(CreateView):
    form_class =  CustomUserCreationForm
    template_name = "registration/freelance.html"
    success_url = "/accounts/login/"
    
    def form_valid(self, form):
        form.instance.is_freelance = True
        return super().form_valid(form)

# create business profile
class BusinessCreateView(CreateView):
    form_class =  CustomUserCreationForm
    template_name = "registration/business.html"
    success_url = "/accounts/login/"
    
    def form_valid(self, form):
        form.instance.is_business = True
        return super().form_valid(form)



class ProfileUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    form_class = UserProfileForm
    template_name = "registration/update-profile.html"
    success_url = reverse_lazy("dashboard:index")
    success_message = 'Profile successfully saved!!!!'

    def get_object(self):
        return Profile.objects.get(pk=self.request.user.pk)


class CreateBusinessProfile(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    form_class =  CompanyProfileForm
    template_name = "registration/company-profile.html"
    success_url = reverse_lazy("dashboard:index")
    success_message = 'Company Created successfully saved!!!!'

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CompanyProfileUpdate(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    form_class =  CompanyProfileForm
    template_name = "registration/update-company-profile.html"
    success_url = reverse_lazy("dashboard:index")
    success_message = 'Profile successfully saved!!!!'

    def get_object(self):
        return CompanyProfile.objects.get(owner=self.request.user.pk)

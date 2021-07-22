from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
# Create your views here.

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


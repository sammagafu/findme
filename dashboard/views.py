from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class DashboardView(TemplateView,LoginRequiredMixin):
    template_name = "dashboard/index.html"

class Profile(TemplateView,LoginRequiredMixin):
    template_name = "dashboard/profile.html"

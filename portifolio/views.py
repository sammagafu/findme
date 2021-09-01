from django.shortcuts import render
from .models import Portfolio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
# Create your views here.

class PortfolioListView(LoginRequiredMixin,ListView):
    model = Portfolio
    template_name = "portfolio/list.html"
    
    
class PortfolioDetail(DetailView):
    model = Portfolio
    context_object_name = "folio"
    template_name="portfolio/details.html"
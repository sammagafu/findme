from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.models import Category
from portifolio.models import Portfolio
# Create your views here.

class Homepage(TemplateView):
    template_name = 'pages/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["portfolio"] = Portfolio.objects.all().order_by('?')[:8]
        return context
    
from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.models import Category
# Create your views here.

class Homepage(TemplateView):
    template_name = 'pages/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context
    
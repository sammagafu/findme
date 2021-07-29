from typing import List
from django.shortcuts import render
from accounts.models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin
from opportunity.models import Opportunity
# Create your views here.
from django.views.generic import ListView,DetailView

class UserListView(LoginRequiredMixin,ListView):
    model = User
    context_object_name = "talent"
    template_name = "talent/list.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_freelance=True)


class UserDetailView(LoginRequiredMixin,DetailView):
    model = User
    context_object_name = "talent"
    template_name = "talent/detail.html"

class AppliedTalents(LoginRequiredMixin,DetailView):
    model = Opportunity
    context_object_name = "talent"
    template_name = "talent/applied.html"
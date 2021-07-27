from typing import List
from django.shortcuts import render
from accounts.models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import ListView,DetailView

class UserListView(ListView,LoginRequiredMixin):
    model = User
    context_object_name = "talent"
    template_name = "talent/list.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_freelance=True)

class UserDetailView(DetailView,LoginRequiredMixin):
    model = User
    context_object_name = "talent"
    template_name = "talent/list.html"
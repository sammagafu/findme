from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import UserProfileForm,CompanyProfileForm
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.


class DashboardView(TemplateView,LoginRequiredMixin):
    template_name = "dashboard/index.html"

class Profile(TemplateView,LoginRequiredMixin):
    template_name = "dashboard/profile.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['userForm'] = UserProfileForm(instance=self.request.user.profile)
        context['companyForm'] = CompanyProfileForm(instance=self.request.user)
        return context


def updateprofile(request):
    if request.method == "POST":
        user_form = UserProfileForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request,('Your profile was successfully updated!'))

    return redirect("dashboard:index")
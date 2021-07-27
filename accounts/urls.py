from django.urls import path
from . import views

app_name = "register"

urlpatterns = [
    path("register/freelancer/",views.FreelanceCreateView.as_view(), name="freelancer"),
    path("register/business/",views.BusinessCreateView.as_view(), name="business"),
    path("update/profile/",views.ProfileUpdateView.as_view(),name="profile"),
    path("create/company-profile/",views.CreateBusinessProfile.as_view(),name="company-profile"),
    path("update/company-profile/",views.CompanyProfileUpdate.as_view(),name="update-profile"),
]

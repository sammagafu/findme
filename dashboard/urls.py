from django import urls
from django.urls import path
from . import views 
from .views import updateprofile
app_name = "dashboard"

urlpatterns = [
    path('',views.DashboardView.as_view(), name="index"),
    path('profile/',views.Profile.as_view(), name="profile"),
    path('update-profile',updateprofile,name="update-profile")
]

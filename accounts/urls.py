from django.urls import path
from . import views

app_name = "register"

urlpatterns = [
    path("register/freelancer/",views.FreelanceCreateView.as_view(), name="freelancer"),
    path("register/business/",views.BusinessCreateView.as_view(), name="business")
]

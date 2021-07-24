from django.urls import path
from . import views
app_name = "talent"

urlpatterns = [
    path('',views.UserListView.as_view(),name="list")
]

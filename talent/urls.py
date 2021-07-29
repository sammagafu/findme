from django.urls import path
from django.views.generic import detail
from . import views
app_name = "talent"

urlpatterns = [
    path('',views.UserListView.as_view(),name="list"),
    path('<int:pk>',views.UserDetailView.as_view(),name="detail"),
    path('<slug>',views.AppliedTalents.as_view(),name="applied")
]

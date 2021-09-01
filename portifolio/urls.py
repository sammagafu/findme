
from django.urls import path
from . import views
app_name = "portifolio"

urlpatterns = [
    path('',views.PortfolioListView.as_view(),name="list"),
    path('<slug>',views.PortfolioDetail.as_view(),name="detail")
]

from django.urls import path
from . import views

app_name = "opportunity"

urlpatterns = [
    path("create/opportunity/",views.OpportunityCreateView.as_view(), name="create"),
    path("bookmarked/",views.MysavedOpportunity.as_view(),name="saved"),
    path("",views.OpportunityListView.as_view(), name="list"),
    path("my-opportunies",views.MyOpportunitiesListView.as_view(),name="my-opportunities"),
    path("<slug>/",views.OpportunityDetailView.as_view(),name="detail"),
    path("<slug>/edit/",views.OpportunityUpdateView.as_view(),name="update"),
    path("bookmark/add/",views.SaveOpportunity.as_view(),name="save"),
    path("apply/this/",views.ApplyFOrjob.as_view(),name="apply"),
    path("applied/done/",views.MyAppliedOpportunity.as_view(),name="applied"),
]

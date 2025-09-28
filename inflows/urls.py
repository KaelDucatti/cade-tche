from django.urls import path

from .views import InflowCreateView, InflowDetailView, InflowListView

app_name = "inflows"

urlpatterns = [
    path("", InflowListView.as_view(), name="list"),
    path("create/", InflowCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", InflowDetailView.as_views(), name="detail"),
]

from django.urls import path

from .views import (
    BrandCreateView,
    BrandDeleteView,
    BrandDetailView,
    BrandListView,
    BrandUpdateView,
)

app_name = "brands"

urlpatterns = [
    path("", BrandListView.as_view(), name="list"),
    path("create/", BrandCreateView.as_view(), name="create"),
    path("<int:pk>/", BrandDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", BrandDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", BrandUpdateView.as_view(), name="update"),
]

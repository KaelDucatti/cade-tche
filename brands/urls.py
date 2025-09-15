from django.urls import path

from .views import (
    BrandCreateView,
    BrandDeleteView,
    BrandDetailView,
    BrandListView,
    BrandUpdateView,
)

urlpatterns = [
    path("brands/list/", BrandListView.as_view(), name="brand_list"),
    path("brands/create/", BrandCreateView.as_view(), name="brand_create"),
    path(
        "brands/detail/<int:pk>/",
        BrandDetailView.as_view(),
        name="brand_detail",
    ),
    path(
        "brands/delete/<int:pk>/",
        BrandDeleteView.as_view(),
        name="brand_delete",
    ),
    path(
        "brands/update/<int:pk>/",
        BrandUpdateView.as_view(),
        name="brand_update",
    ),
]

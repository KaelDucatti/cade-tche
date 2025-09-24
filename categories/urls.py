from django.urls import path

from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
)

app_name = "categories"

urlpatterns = [
    path("", CategoryListView.as_view(), name="list"),
    path("create/", CategoryCreateView.as_view(), name="create"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CategoryUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="delete"),
]

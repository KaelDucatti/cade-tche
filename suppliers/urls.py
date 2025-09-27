from django.urls import path

app_name = "suppliers"

urlpatterns = [
    path("", ..., name="list"),
    path("create/", ..., name="create"),
    path("<int:pk>/", ..., name="detail"),
    path("<int:pk>/update/", ..., name="update"),
    path("<int:pk>/delete/", ..., name="delete"),
]
